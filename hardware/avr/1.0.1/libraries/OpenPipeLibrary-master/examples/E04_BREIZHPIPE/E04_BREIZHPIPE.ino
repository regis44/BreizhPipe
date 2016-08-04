#include <Wire.h>     // Wire library for comunicating with OpenPipe
#include <OpenPipe.h> // OpenPipe Library
#include <MIDIUSB.h>  // The USB MIDI Library

// Select here which fingering to use
#define FINGERING FINGERING_GAITA_GALEGA
//#define FINGERING FINGERING_GAITA_ASTURIANA
//#define FINGERING FINGERING_GREAT_HIGHLAND_BAGPIPE
//#define FINGERING FINGERING_UILLEANN_PIPE
//#define FINGERING FINGERING_SACKPIPA

// Select here which MIDI instrument to use
// http://en.wikipedia.org/wiki/General_MIDI
#define MIDI_INSTRUMENT 66 // Tenor Sax

// Global variables
unsigned long fingers, previous_fingers;
unsigned char previous_note;
char playing;

#define LED   6
#define VBAT  A0
#define PWM   5
#define IRQ   7

int vBat = 0;

//MIDI_CREATE_DEFAULT_INSTANCE();

void setup(){

  // OpenPipe setup
  OpenPipe.config();
  OpenPipe.setFingering(FINGERING);
  pinMode(LED, OUTPUT);
  digitalWrite(LED, HIGH);
  digitalWrite(PWM, OUTPUT);
  digitalWrite(IRQ, OUTPUT);
  vBat = analogRead(VBAT);

  Serial.begin(115200); //Use this line for Hairless MIDI<->Serial Bridge
  Serial.println("BreizhPipe Project...");

  //MIDI.sendProgramChange(MIDI_INSTRUMENT,1); // Select MIDI instrument

  // Variables initialization
  fingers=0;
  previous_fingers=0xFF;
  playing=false;
}

void noteOn(byte channel, byte pitch, byte velocity) {
  midiEventPacket_t noteOn = {0x09, 0x90 | channel, pitch, velocity};
  MidiUSB.sendMIDI(noteOn);
}

void noteOff(byte channel, byte pitch, byte velocity) {
  midiEventPacket_t noteOff = {0x08, 0x80 | channel, pitch, velocity};
  MidiUSB.sendMIDI(noteOff);
}

void loop(){
  // Read OpenPipe fingers
  fingers=OpenPipe.readFingers();

  // If fingers have changed...
  if (fingers!=previous_fingers){
    previous_fingers=fingers;

    // Check the low right thumb sensor
    if (OpenPipe.isON()){
      playing=true;

      // If note changed...
      if (OpenPipe.note!=previous_note && OpenPipe.note!=0xFF){
         noteOff(1,previous_note,127);   // Stop the previous note
         MidiUSB.flush();
         noteOn(1,OpenPipe.note,127);   // Start the current note
         MidiUSB.flush();
         previous_note=OpenPipe.note;
      }
    }else{
      if (playing){
         noteOff(1,OpenPipe.note,0);   // Stop the note
         MidiUSB.flush();
         playing = false;
      }
    }
  }
}
