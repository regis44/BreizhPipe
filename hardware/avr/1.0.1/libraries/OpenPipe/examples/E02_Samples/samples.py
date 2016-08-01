#!/usr/bin/env python

#	Copyright (c) 2016 Xulio Coira <xulioc@gmail.com>. All rights reserved.
#
#	This program is free software: you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation, either version 3 of the License, or
#	(at your option) any later version.
#
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with this program.  If not, see <http://www.gnu.org/licenses/>.

import math
import sys

BITS=8
SAMPLE_RATE=44100
SIGNED=False

# SINUSOIDS
sinusoids=(
	("SINUSOIDS"), #INSTRUMENT NAME
	(48, 130, 1.0, (1,)),
	(49, 139, 1.0, (1,)),
	(50, 147, 1.0, (1,)),
	(51, 156, 1.0, (1,)),
	(52, 165, 1.0, (1,)),
	(53, 175, 1.0, (1,)),
	(54, 185, 1.0, (1,)),
	(55, 196, 1.0, (1,)),
	(56, 208, 1.0, (1,)),
	(57, 220, 1.0, (1,)),
	(58, 233, 1.0, (1,)),
	(59, 247, 1.0, (1,)),
	(60, 262, 1.0, (1,)),
	(61, 277, 1.0, (1,)),
	(62, 294, 1.0, (1,)),
	(63, 311, 1.0, (1,)),
	(64, 330, 1.0, (1,)),
	(65, 349, 1.0, (1,)),
	(66, 370, 1.0, (1,)),
	(67, 392, 1.0, (1,)),
	(68, 415, 1.0, (1,)),
	(69, 440, 1.0, (1,)),
	(70, 466, 1.0, (1,)),
	(71, 494, 1.0, (1,)),
	(72, 523, 1.0, (1,)),
	(73, 554, 1.0, (1,)),
	(74, 587, 1.0, (1,)),
	(75, 622, 1.0, (1,)),
	(76, 659, 1.0, (1,)),
	(77, 698, 1.0, (1,)),
	(78, 740, 1.0, (1,)),
	(79, 784, 1.0, (1,)),
	(80, 831, 1.0, (1,)),
	(81, 880, 1.0, (1,)),
	(82, 932, 1.0, (1,)),
	(83, 988, 1.0, (1,)),
	(84, 1046, 1.0, (1,)),
	(85, 1108, 1.0, (1,)),
	(86, 1174, 1.0, (1,)),
	(87, 1244, 1.0, (1,)),
	(88, 1318, 1.0, (1,)),
	(89, 1396, 1.0, (1,)),
	(90, 1480, 1.0, (1,)),
)

#GAITA GALEGA
gaita_galega=(
	("GAITA_GALEGA"), #INSTRUMENT NAME
	(48, 130.8128, 1, (1.0, 0.5131, 0.9251, 0.7995, 0.9317, 0.3742, 0.0386, 0.1261, 0.0574, 0.0361, 0.0332, 0.0145, 0.0112, 0.0109, 0.0049, 0.0094, 0.013, 0.0317, 0.0137, 0.0544)),
	(60, 261.6256, 1, (0.4855, 0.5149, 0.4062, 0.2259, 0.2127, 1.0, 0.0408, 0.1016, 0.0239, 0.0462, 0.2333, 0.1041, 0.0934, 0.009, 0.0564, 0.0171, 0.1189, 0.1485, 0.0447, 0.0382)),
	(71, 493.8833, 1, (0.3976, 0.6409, 0.4899, 1.0, 0.3137, 0.1548, 0.2085, 0.2972, 0.1409, 0.0243, 0.0411, 0.0668, 0.0734, 0.0875, 0.0509, 0.0428, 0.0126, 0.0476, 0.0782, 0.0916)),
	(72, 523.2511, 1, (0.4623, 0.8685, 0.7808, 1.0, 0.681, 0.1535, 0.3219, 0.503, 0.3814, 0.038, 0.1563, 0.1045, 0.073, 0.0265, 0.0269, 0.0263, 0.055, 0.1148, 0.2005, 0.1315)),
	(73, 554.3700, 1, (0.4623, 0.8685, 0.7808, 1.0, 0.681, 0.1535, 0.3219, 0.503, 0.3814, 0.038, 0.1563, 0.1045, 0.073, 0.0265, 0.0269, 0.0263, 0.055, 0.1148, 0.2005, 0.1315)),
	(74, 587.3295, 1, (0.5589, 0.6633, 0.7047, 1.0, 0.3202, 0.1594, 0.6539, 0.1778, 0.1456, 0.0314, 0.0546, 0.0649, 0.0438, 0.0161, 0.0325, 0.0187, 0.1526, 0.1778, 0.0968, 0.078)),
	(75, 622.2500, 1, (0.5589, 0.6633, 0.7047, 1.0, 0.3202, 0.1594, 0.6539, 0.1778, 0.1456, 0.0314, 0.0546, 0.0649, 0.0438, 0.0161, 0.0325, 0.0187, 0.1526, 0.1778, 0.0968, 0.078)),
	(76, 659.2551, 1, (0.3047, 0.4057, 0.7287, 1.0, 0.1276, 0.556, 0.103, 0.0657, 0.0437, 0.0436, 0.0162, 0.0078, 0.0182, 0.0256, 0.0649, 0.0721, 0.0189, 0.0363, 0.0278, 0.0277)),
	(77, 698.4565, 1, (0.397, 0.6125, 1.0, 0.2904, 0.3445, 0.3505, 0.3175, 0.1612, 0.1339, 0.0623, 0.044, 0.039, 0.0386, 0.0172, 0.1171, 0.076, 0.1353, 0.0821, 0.0826, 0.0921)),
	(78, 739.9900, 1, (0.397, 0.6125, 1.0, 0.2904, 0.3445, 0.3505, 0.3175, 0.1612, 0.1339, 0.0623, 0.044, 0.039, 0.0386, 0.0172, 0.1171, 0.076, 0.1353, 0.0821, 0.0826, 0.0921)),
	(79, 783.9909, 1, (0.1833, 0.3204, 1.0, 0.6586, 0.3577, 0.0487, 0.0459, 0.0309, 0.0359, 0.0279, 0.0396, 0.028, 0.0578, 0.0866, 0.1601, 0.1364, 0.0622, 0.0372, 0.0168, 0.0099)),
	(80, 830.6100, 1, (0.1833, 0.3204, 1.0, 0.6586, 0.3577, 0.0487, 0.0459, 0.0309, 0.0359, 0.0279, 0.0396, 0.028, 0.0578, 0.0866, 0.1601, 0.1364, 0.0622, 0.0372, 0.0168, 0.0099)),
	(81, 880.0000, 1, (0.2423, 0.4105, 1.0, 0.196, 0.246, 0.2087, 0.1997, 0.0206, 0.0279, 0.0514, 0.0892, 0.1065, 0.1298, 0.1729, 0.0758, 0.0443, 0.0366, 0.0155, 0.012, 0.0102)),
	(82, 932.3300, 1, (0.2423, 0.4105, 1.0, 0.196, 0.246, 0.2087, 0.1997, 0.0206, 0.0279, 0.0514, 0.0892, 0.1065, 0.1298, 0.1729, 0.0758, 0.0443, 0.0366, 0.0155, 0.012, 0.0102)),
	(83, 987.7666, 1, (0.336, 0.4945, 1.0, 0.3454, 0.2002, 0.0763, 0.0705, 0.0253, 0.0754, 0.0422, 0.2107, 0.3412, 0.2618, 0.1425, 0.0864, 0.0299, 0.0223, 0.0375, 0.0464, 0.0596)),
	(84, 1046.5023, 1, (0.4391, 1.0, 0.4572, 0.2788, 0.0629, 0.1973, 0.0596, 0.0133, 0.0569, 0.0371, 0.0557, 0.0333, 0.0205, 0.0279, 0.0186, 0.006, 0.0058, 0.0051, 0.0064, 0.0035)),
	(85, 1108.7000, 1, (0.4391, 1.0, 0.4572, 0.2788, 0.0629, 0.1973, 0.0596, 0.0133, 0.0569, 0.0371, 0.0557, 0.0333, 0.0205, 0.0279, 0.0186, 0.006, 0.0058, 0.0051, 0.0064, 0.0035)),
	(86, 1174.7000, 1, (0.4391, 1.0, 0.4572, 0.2788, 0.0629, 0.1973, 0.0596, 0.0133, 0.0569, 0.0371, 0.0557, 0.0333, 0.0205, 0.0279, 0.0186, 0.006, 0.0058, 0.0051, 0.0064, 0.0035)),
	(87, 1244.5000, 1, (0.4391, 1.0, 0.4572, 0.2788, 0.0629, 0.1973, 0.0596, 0.0133, 0.0569, 0.0371, 0.0557, 0.0333, 0.0205, 0.0279, 0.0186, 0.006, 0.0058, 0.0051, 0.0064, 0.0035)),
	(88, 1318.5000, 1, (0.4391, 1.0, 0.4572, 0.2788, 0.0629, 0.1973, 0.0596, 0.0133, 0.0569, 0.0371, 0.0557, 0.0333, 0.0205, 0.0279, 0.0186, 0.006, 0.0058, 0.0051, 0.0064, 0.0035)),
	(89, 1396.9000, 1, (0.4391, 1.0, 0.4572, 0.2788, 0.0629, 0.1973, 0.0596, 0.0133, 0.0569, 0.0371, 0.0557, 0.0333, 0.0205, 0.0279, 0.0186, 0.006, 0.0058, 0.0051, 0.0064, 0.0035)),
	(90, 1480.0000, 1, (0.4391, 1.0, 0.4572, 0.2788, 0.0629, 0.1973, 0.0596, 0.0133, 0.0569, 0.0371, 0.0557, 0.0333, 0.0205, 0.0279, 0.0186, 0.006, 0.0058, 0.0051, 0.0064, 0.0035)),
)

#GAITA ASTURIANA
gaita_asturiana=(
	("GAITA_ASTURIANA"), #INSTRUMENT NAME
(48, 130.6407, 1.0000, (0.431, 0.6793, 0.4626, 0.8202, 0.3112, 1.0, 0.6185, 0.3416, 0.4307, 0.3177, 0.2185, 0.1176, 0.2072, 0.1138, 0.0585, 0.1069, 0.1292, 0.0568, 0.0594, 0.1595, 0.153, 0.0513, 0.0595, 0.0595, 0.015, 0.0363, 0.0231, 0.0205, 0.0275, 0.0167, 0.0198, 0.0233, 0.0181, 0.018, 0.0193, 0.0159, 0.0134, 0.013, 0.0108, 0.0092, 0.0102, 0.0095, 0.012, 0.0125, 0.0133, 0.013, 0.0136, 0.0124, 0.0125, 0.0118, 0.012, 0.0095, 0.0098, 0.0083, 0.0078, 0.0087, 0.0087, 0.0104, 0.0107, 0.0114)), #RONCO.wav
(71, 494.1032, 0.5413, (0.1496, 0.4905, 0.7607, 1.0, 0.9087, 0.8412, 0.3647, 0.1652, 0.2997, 0.1511, 0.2209, 0.0673, 0.099, 0.1118, 0.0677, 0.0701, 0.0527, 0.0451, 0.039, 0.0412, 0.0328, 0.0353, 0.0287, 0.0196, 0.031, 0.0353, 0.0261, 0.0203, 0.0256, 0.0198, 0.0169, 0.0138, 0.0018, 0.0021, 0.0024, 0.0027, 0.0029, 0.0032, 0.0034, 0.0035, 0.0037, 0.0038, 0.004, 0.0038, 0.0005, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)), #SI.wav
(72, 523.2614, 0.1648, (0.2035, 0.4073, 0.7275, 1.0, 0.9878, 0.4848, 0.1153, 0.2413, 0.1155, 0.1066, 0.0752, 0.1004, 0.1306, 0.054, 0.0597, 0.0199, 0.0284, 0.0177, 0.0861, 0.036, 0.0767, 0.0485, 0.0506, 0.0305, 0.0153, 0.0165, 0.0192, 0.0092, 0.0095, 0.0071, 0.0013, 0.0015, 0.0016, 0.0018, 0.0019, 0.0022, 0.0024, 0.0024, 0.0027, 0.0027, 0.0029, 0.0018, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)), #DO.wav
(73, 553.3566, 0.3529, (0.2463, 0.3567, 0.5397, 1.0, 0.2002, 0.1296, 0.1201, 0.0607, 0.0535, 0.065, 0.0332, 0.0396, 0.0536, 0.0563, 0.0189, 0.0066, 0.012, 0.0517, 0.0355, 0.0526, 0.0388, 0.0174, 0.0103, 0.0109, 0.0085, 0.0086, 0.0066, 0.005, 0.0018, 0.0009, 0.0011, 0.0012, 0.0014, 0.0015, 0.0016, 0.0017, 0.0018, 0.0019, 0.0019, 0.0006, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)), #DO#.wav
(74, 585.6843, 0.5365, (0.3685, 1.0, 0.8569, 0.9227, 0.735, 0.6618, 0.4295, 0.2039, 0.2555, 0.1155, 0.0596, 0.0559, 0.0614, 0.0582, 0.1101, 0.0356, 0.0775, 0.0389, 0.0347, 0.0385, 0.0221, 0.0127, 0.0176, 0.0192, 0.0222, 0.0171, 0.0115, 0.002, 0.0022, 0.0025, 0.0028, 0.0032, 0.0034, 0.0036, 0.0039, 0.0038, 0.004, 0.0006, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)), #RE.wav
(75, 620.9630, 0.2816, (0.2542, 0.6604, 0.8862, 0.4325, 1.0, 0.7018, 0.2378, 0.075, 0.144, 0.1258, 0.3313, 0.239, 0.1604, 0.0753, 0.1118, 0.0811, 0.2224, 0.1156, 0.0596, 0.0305, 0.0331, 0.0176, 0.0224, 0.0189, 0.0093, 0.002, 0.0015, 0.0019, 0.002, 0.0023, 0.0025, 0.0027, 0.0028, 0.0029, 0.003, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)), #MIb.wav
(76, 659.3968, 0.6758, (0.0816, 0.3852, 1.0, 0.0994, 0.0597, 0.0823, 0.0987, 0.0805, 0.066, 0.0371, 0.1234, 0.0577, 0.0221, 0.0342, 0.0337, 0.0567, 0.0951, 0.0262, 0.0218, 0.0159, 0.0082, 0.0076, 0.0089, 0.001, 0.0012, 0.0014, 0.0015, 0.0017, 0.002, 0.002, 0.0021, 0.0023, 0.0022, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)), #MI.wav
(77, 697.2876, 0.3761, (0.1948, 1.0, 0.3499, 0.2637, 0.2628, 0.0387, 0.0924, 0.174, 0.17, 0.1823, 0.1239, 0.065, 0.0471, 0.0515, 0.1249, 0.1116, 0.0572, 0.0363, 0.0252, 0.0083, 0.0135, 0.0074, 0.0009, 0.0011, 0.0013, 0.0014, 0.0015, 0.0017, 0.0017, 0.002, 0.0021, 0.0002, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)), #FA.wav
(78, 737.1099, 0.3526, (0.1715, 0.5018, 1.0, 0.3734, 0.6683, 0.295, 0.1292, 0.1017, 0.2403, 0.3362, 0.1032, 0.0309, 0.0733, 0.2086, 0.2, 0.0468, 0.0344, 0.0324, 0.0084, 0.011, 0.007, 0.001, 0.0012, 0.0014, 0.0016, 0.0018, 0.0019, 0.002, 0.0021, 0.0009, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)), #FA#.wav
(79, 782.9253, 0.5539, (0.2605, 0.3546, 1.0, 0.502, 0.1061, 0.1747, 0.1132, 0.0468, 0.2075, 0.1244, 0.1408, 0.028, 0.0878, 0.1296, 0.0791, 0.0291, 0.031, 0.0146, 0.0109, 0.001, 0.0013, 0.0016, 0.0019, 0.0022, 0.0023, 0.0025, 0.0026, 0.0017, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)), #SOL.wav
(80, 830.5805, 0.2971, (0.5002, 0.6777, 1.0, 0.5299, 0.2051, 0.0982, 0.1085, 0.2957, 0.1817, 0.2262, 0.296, 0.0289, 0.1535, 0.0837, 0.0473, 0.0331, 0.0302, 0.0188, 0.0048, 0.0018, 0.0024, 0.0026, 0.003, 0.0033, 0.0034, 0.0035, 0.0002, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)), #SOL#.wav
(81, 878.7180, 0.4239, (0.7464, 1.0, 0.7664, 0.3108, 0.5444, 0.1195, 0.3308, 0.4945, 0.2857, 0.1501, 0.2573, 0.4108, 0.1761, 0.1369, 0.039, 0.0342, 0.0072, 0.0019, 0.0024, 0.003, 0.0035, 0.004, 0.0045, 0.0047, 0.0028, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)), #LA.wav
(82, 928.6231, 0.4533, (0.6196, 0.9778, 0.6313, 0.375, 0.6118, 1.0, 0.1905, 0.3208, 0.2542, 0.1509, 0.0596, 0.1176, 0.1056, 0.0477, 0.0303, 0.0169, 0.0087, 0.0013, 0.0016, 0.0019, 0.0022, 0.0024, 0.0025, 0.0006, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)), #SIb2.wav
(83, 989.1061, 0.4243, (0.293, 1.0, 0.4193, 0.1263, 0.093, 0.0882, 0.1208, 0.0892, 0.1266, 0.0167, 0.166, 0.0351, 0.0313, 0.0514, 0.0105, 0.0141, 0.0013, 0.0016, 0.0018, 0.0021, 0.0022, 0.0018, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)), #SI2.wav
(84, 1045.2169, 0.6426, (0.1354, 1.0, 0.6321, 0.1205, 0.0674, 0.0722, 0.1016, 0.1163, 0.0874, 0.0128, 0.0471, 0.0154, 0.0175, 0.0069, 0.0066, 0.0015, 0.0019, 0.0023, 0.0026, 0.0028, 0.0018, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)), #DO2.wav
(85, 1106.4910, 0.5686, (0.3247, 1.0, 0.2299, 0.1243, 0.2313, 0.0435, 0.0963, 0.0875, 0.0107, 0.0545, 0.0835, 0.0233, 0.0111, 0.0072, 0.0015, 0.002, 0.0024, 0.0028, 0.0029, 0.0013, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)), #SOL#2.wav
(86, 1174.2447, 0.4773, (0.8389, 1.0, 0.5081, 0.4066, 0.1475, 0.1407, 0.0508, 0.0533, 0.1115, 0.0383, 0.066, 0.0146, 0.0104, 0.0027, 0.0036, 0.0043, 0.005, 0.0054, 0.0016, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)), #RE2.wav
(87, 1241.9067, 0.3551, (0.5018, 1.0, 0.576, 0.1347, 0.0895, 0.1955, 0.0324, 0.0584, 0.14, 0.0244, 0.0139, 0.017, 0.0021, 0.003, 0.0036, 0.0043, 0.0047, 0.0013, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)), #MIb2.wav
(88, 1319.1737, 0.6893, (1.0, 0.5875, 0.324, 0.4338, 0.4156, 0.2727, 0.2086, 0.288, 0.0865, 0.0258, 0.0313, 0.0056, 0.0029, 0.0038, 0.0044, 0.0049, 0.0011, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)), #MI2.wav
(89, 1396.4119, 0.7151, (1.0, 0.3773, 0.6308, 0.246, 0.6586, 0.3945, 0.2321, 0.0788, 0.0592, 0.044, 0.0171, 0.0037, 0.0049, 0.006, 0.0066, 0.002, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)), #FA2.wav
(91, 1562.4391, 0.4631, (1.0, 0.836, 0.4256, 0.1888, 0.1929, 0.0736, 0.0586, 0.0404, 0.0367, 0.0124, 0.0027, 0.0035, 0.0042, 0.0028, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)), #SOL2.wav
)

#GREAT HIGHLAND BAGPIPE
ghb=(
	("GHB"), #INSTRUMENT NAME
	(67, 414, 1.00, (1.12202, 1.00577, 1.03039, 1.01508, 1.06660, 1.01508, 1.02920, 1.00346, 1.00809)), #LOW G
	(69, 466, 1.00, (1.12202, 1.00577, 1.03039, 1.01508, 1.06660, 1.01508, 1.02920, 1.00346, 1.00809)), #LOW A
	(71, 524, 0.92, (1.12202, 1.00577, 1.03039, 1.01508, 1.06660, 1.01508, 1.02920, 1.00346, 1.00809)), #B
	(72, 559, 0.92, (1.12202, 1.00577, 1.03039, 1.01508, 1.06660, 1.01508, 1.02920, 1.00346, 1.00809)), #CNAT
	(73, 583, 0.92, (1.12202, 1.00577, 1.03039, 1.01508, 1.06660, 1.01508, 1.02920, 1.00346, 1.00809)), #C
	(74, 621, 0.92, (1.12202, 1.00577, 1.03039, 1.01508, 1.06660, 1.01508, 1.02920, 1.00346, 1.00809)), #D
	(76, 699, 0.92, (1.12202, 1.00577, 1.03039, 1.01508, 1.06660, 1.01508, 1.02920, 1.00346, 1.00809)), #E
	(77, 746, 0.92, (1.12202, 1.00577, 1.03039, 1.01508, 1.06660, 1.01508, 1.02920, 1.00346, 1.00809)), #FNAT
	(78, 777, 0.92, (1.12202, 1.00577, 1.03039, 1.01508, 1.06660, 1.01508, 1.02920, 1.00346, 1.00809)), #F
	(79, 839, 0.92, (1.12202, 1.00577, 1.03039, 1.01508, 1.06660, 1.01508, 1.02920, 1.00346, 1.00809)), #HIGH G
	(81, 932, 0.92, (1.12202, 1.00577, 1.03039, 1.01508, 1.06660, 1.01508, 1.02920, 1.00346, 1.00809)), #HIGH A
)

#UILLEANN PIPE
uilleann=(
	("UILLEANN"), #INSTRUMENT NAME
	(62, 293.664800, 0.900000, (0.1927, 0.1823, 0.3063, 0.0636, 0.3095, 0.1262, 1.0, 0.3796, 0.1657, 0.1447, 0.2947, 0.3117, 0.4147, 0.1501, 0.1341, 0.1541, 0.1074, 0.0412, 0.1597, 0.0937)),
	(64, 329.627600, 0.246011, (0.5257, 0.438, 1.0, 0.0951, 0.069, 0.133, 0.0819, 0.0743, 0.1443, 0.1288, 0.0538, 0.0362, 0.032, 0.031, 0.0506, 0.0283, 0.029, 0.0455, 0.0788, 0.1006)),
	(66, 369.994400, 0.327083, (1.0, 0.3406, 0.3785, 0.1763, 0.7677, 0.135, 0.412, 0.6037, 0.1829, 0.0768, 0.1556, 0.2061, 0.08, 0.0551, 0.1131, 0.0813, 0.0425, 0.0595, 0.0485, 0.0732)),
	(67, 391.995400, 0.224712, (0.8865, 0.4776, 0.5571, 0.6191, 0.9857, 0.6464, 1.0, 0.8278, 0.2776, 0.3947, 0.1898, 0.0721, 0.0532, 0.0833, 0.1581, 0.0716, 0.0896, 0.0997, 0.1662, 0.0685)),
	(69, 440.000000, 0.397436, (0.3036, 1.0, 0.3764, 0.6252, 0.1827, 0.5222, 0.2788, 0.3001, 0.2717, 0.4998, 0.2714, 0.0435, 0.1276, 0.1962, 0.0708, 0.0378, 0.22, 0.0889, 0.0446, 0.049)),
	(71, 493.883300, 0.373936, (0.3621, 1.0, 0.5575, 0.903, 0.9346, 0.4813, 0.6476, 0.1648, 0.2847, 0.1136, 0.1049, 0.1354, 0.2159, 0.2055, 0.1633, 0.0871, 0.1094, 0.1985, 0.0771, 0.267)),
	(72, 523.251100, 0.640920, (0.1772, 1.0, 0.1662, 0.8125, 0.3236, 0.2936, 0.1408, 0.3552, 0.1199, 0.0765, 0.2041, 0.0851, 0.332, 0.144, 0.1427, 0.0617, 0.1254, 0.0934, 0.0574, 0.0983)),
	(73, 554.365300, 0.565789, (0.43, 0.8382, 0.1641, 1.0, 0.8736, 0.2243, 0.392, 0.1339, 0.0992, 0.1925, 0.1583, 0.1314, 0.2845, 0.2175, 0.1119, 0.0386, 0.0481, 0.0877, 0.0592, 0.0588)),
	(74, 587.329500, 0.552577, (0.5028, 1.0, 0.114, 0.3768, 0.0804, 0.163, 0.283, 0.0489, 0.1808, 0.0718, 0.0605, 0.2813, 0.1284, 0.2264, 0.0771, 0.0557, 0.0693, 0.0346, 0.0128, 0.1692)),
	(76, 659.255100, 0.531010, (1.0, 0.189, 0.7354, 0.1168, 0.0615, 0.0708, 0.1303, 0.0731, 0.179, 0.0528, 0.0854, 0.1505, 0.1536, 0.0474, 0.0355, 0.0225, 0.0213, 0.0347, 0.0278, 0.0171)),
	(78, 739.988800, 0.364096, (0.4555, 0.2293, 0.6203, 1.0, 0.4607, 0.0608, 0.2422, 0.196, 0.0796, 0.4421, 0.2225, 0.0898, 0.1786, 0.0671, 0.0772, 0.0651, 0.087, 0.0696, 0.0126, 0.0194)),
	(79, 783.990900, 1.000000, (0.2299, 0.0725, 1.0, 0.2973, 0.2252, 0.0578, 0.0356, 0.0749, 0.0331, 0.0847, 0.181, 0.0402, 0.0366, 0.0368, 0.0319, 0.0373, 0.0306, 0.0238, 0.0305, 0.0346)),
	(81, 880.000000, 0.704352, (1.0, 0.2027, 0.5352, 0.2478, 0.3091, 0.1283, 0.103, 0.1671, 0.171, 0.0975, 0.0722, 0.0672, 0.0674, 0.0527, 0.0602, 0.0842, 0.033, 0.0641, 0.0517, 0.0374)),
	(83, 987.766600, 0.532811, (1.0, 0.2195, 0.5825, 0.4962, 0.08, 0.2161, 0.2794, 0.1678, 0.1925, 0.2078, 0.1308, 0.0485, 0.0602, 0.0755, 0.0668, 0.051, 0.036, 0.0289, 0.0236, 0.0199)),
	(84, 1046.502300, 0.547334, (1.0, 0.2296, 0.6172, 0.3559, 0.1826, 0.2921, 0.1797, 0.2354, 0.1607, 0.0957, 0.0811, 0.1027, 0.1523, 0.0517, 0.1073, 0.0758, 0.0541, 0.0657, 0.0285, 0.0234)),
)

#sackpipa detuned
sackpipa_detuned=(
("SACKPIPA"), #INSTRUMENT NAME
(45, 113.2212, 1, (0.5867, 0.989, 0.5427, 0.3963, 0.9262, 0.9863, 0.6459, 1.0, 0.26, 0.2212, 0.3047, 0.3317, 0.2036, 0.4272, 0.2559, 0.329, 0.5104, 0.9461, 0.3296, 0.2631)) ,
(62, 295.8923, 1, (0.4751, 0.0971, 1.0, 0.4491, 0.244, 0.2512, 0.093, 0.2819, 0.4429, 0.392, 0.1906, 0.2321, 0.2884, 0.1409, 0.1589, 0.0537, 0.0749, 0.052, 0.0657, 0.0115)) ,
(64, 337.5378, 1, (0.7019, 0.5234, 1.0, 0.3028, 0.8385, 0.4458, 0.5286, 0.5383, 0.6831, 0.7238, 0.2434, 0.1962, 0.1599, 0.1923, 0.1367, 0.188, 0.1472, 0.2106, 0.159, 0.2066)) ,
(66, 378.2219, 1, (0.6856, 0.5059, 0.5974, 0.7877, 0.4496, 0.3707, 1.0, 0.2702, 0.9744, 0.3315, 0.4127, 0.1585, 0.2092, 0.2266, 0.0921, 0.2314, 0.1382, 0.0961, 0.3153, 0.0453)) ,
#(68, 405.4066, 1, (1.0, 0.2129, 0.3087, 0.574, 0.6789, 0.4138, 0.5408, 0.2413, 0.7095, 0.1461, 0.4125, 0.1761, 0.188, 0.2505, 0.1773, 0.3121, 0.1623, 0.3619, 0.0709, 0.1003)) ,
(68, 424.9346, 1, (0.3656, 0.2246, 0.6677, 0.4353, 1.0, 0.3694, 0.5821, 0.8508, 0.1123, 0.3429, 0.0601, 0.16, 0.0946, 0.3299, 0.1084, 0.2328, 0.9328, 0.087, 0.0884, 0.0916)) ,
(69, 451.3955, 1, (0.1602, 0.1162, 0.1141, 0.1309, 0.0573, 1.0, 0.0616, 0.3066, 0.0237, 0.2895, 0.0483, 0.0657, 0.0883, 0.1795, 0.0461, 0.1759, 0.0219, 0.0402, 0.0147, 0.0329)) ,
(71, 506.8997, 1, (0.2726, 1.0, 0.7021, 0.6089, 0.4949, 0.5292, 0.2296, 0.3866, 0.5391, 0.622, 0.2475, 0.2965, 0.1202, 0.1713, 0.1114, 0.0795, 0.1619, 0.2331, 0.0999, 0.0314)) ,
(72, 521.3922, 1, (0.3077, 0.597, 0.5168, 0.8648, 0.48, 0.319, 1.0, 0.4615, 0.5621, 0.1374, 0.1047, 0.3261, 0.1692, 0.1096, 0.1422, 0.0687, 0.085, 0.0601, 0.0614, 0.0851)) ,
(73, 555.8725, 1, (0.5056, 0.4658, 0.7351, 0.2136, 0.3969, 0.2432, 1.0, 0.7641, 0.3892, 0.6943, 0.2252, 0.1525, 0.3561, 0.1073, 0.0797, 0.0786, 0.1052, 0.0892, 0.0683, 0.0217)) ,
(75, 611.7707, 1, (0.6212, 0.3164, 1.0, 0.4124, 0.3473, 0.1649, 0.5741, 0.3429, 0.2616, 0.1776, 0.2784, 0.1268, 0.1987, 0.0857, 0.1405, 0.2199, 0.016, 0.0517, 0.0822, 0.0461)) ,
(77, 683.9311, 1, (0.9703, 0.2828, 0.8853, 0.7901, 1.0, 0.6872, 0.2561, 0.6743, 0.3603, 0.2284, 0.3726, 0.1408, 0.0767, 0.0655, 0.1344, 0.0987, 0.1835, 0.1671, 0.0997, 0.034)) ,
)


#sackpipa
sackpipa=(
("SACKPIPA"), #INSTRUMENT NAME
(45, 110.0, 1, (0.5867, 0.989, 0.5427, 0.3963, 0.9262, 0.9863, 0.6459, 1.0, 0.26, 0.2212, 0.3047, 0.3317, 0.2036, 0.4272, 0.2559, 0.329, 0.5104, 0.9461, 0.3296, 0.2631)) ,
(62, 293.6648, 1, (0.4751, 0.0971, 1.0, 0.4491, 0.244, 0.2512, 0.093, 0.2819, 0.4429, 0.392, 0.1906, 0.2321, 0.2884, 0.1409, 0.1589, 0.0537, 0.0749, 0.052, 0.0657, 0.0115)) ,
(64, 329.6276, 1, (0.7019, 0.5234, 1.0, 0.3028, 0.8385, 0.4458, 0.5286, 0.5383, 0.6831, 0.7238, 0.2434, 0.1962, 0.1599, 0.1923, 0.1367, 0.188, 0.1472, 0.2106, 0.159, 0.2066)) ,
(66, 369.9944, 1, (0.6856, 0.5059, 0.5974, 0.7877, 0.4496, 0.3707, 1.0, 0.2702, 0.9744, 0.3315, 0.4127, 0.1585, 0.2092, 0.2266, 0.0921, 0.2314, 0.1382, 0.0961, 0.3153, 0.0453)) ,
#(68, 415.3047, 1, (1.0, 0.2129, 0.3087, 0.574, 0.6789, 0.4138, 0.5408, 0.2413, 0.7095, 0.1461, 0.4125, 0.1761, 0.188, 0.2505, 0.1773, 0.3121, 0.1623, 0.3619, 0.0709, 0.1003)) ,
(68, 415.3047, 1, (0.3656, 0.2246, 0.6677, 0.4353, 1.0, 0.3694, 0.5821, 0.8508, 0.1123, 0.3429, 0.0601, 0.16, 0.0946, 0.3299, 0.1084, 0.2328, 0.9328, 0.087, 0.0884, 0.0916)) ,
(69, 440.0, 1, (0.1602, 0.1162, 0.1141, 0.1309, 0.0573, 1.0, 0.0616, 0.3066, 0.0237, 0.2895, 0.0483, 0.0657, 0.0883, 0.1795, 0.0461, 0.1759, 0.0219, 0.0402, 0.0147, 0.0329)) ,
(71, 493.8833, 1, (0.2726, 1.0, 0.7021, 0.6089, 0.4949, 0.5292, 0.2296, 0.3866, 0.5391, 0.622, 0.2475, 0.2965, 0.1202, 0.1713, 0.1114, 0.0795, 0.1619, 0.2331, 0.0999, 0.0314)) ,
(72, 523.2511, 1, (0.3077, 0.597, 0.5168, 0.8648, 0.48, 0.319, 1.0, 0.4615, 0.5621, 0.1374, 0.1047, 0.3261, 0.1692, 0.1096, 0.1422, 0.0687, 0.085, 0.0601, 0.0614, 0.0851)) ,
(73, 554.3653, 1, (0.5056, 0.4658, 0.7351, 0.2136, 0.3969, 0.2432, 1.0, 0.7641, 0.3892, 0.6943, 0.2252, 0.1525, 0.3561, 0.1073, 0.0797, 0.0786, 0.1052, 0.0892, 0.0683, 0.0217)) ,
#(74, 554.3653, 1, (0.5056, 0.4658, 0.7351, 0.2136, 0.3969, 0.2432, 1.0, 0.7641, 0.3892, 0.6943, 0.2252, 0.1525, 0.3561, 0.1073, 0.0797, 0.0786, 0.1052, 0.0892, 0.0683, 0.0217)) ,
(75, 622.254, 1, (0.6212, 0.3164, 1.0, 0.4124, 0.3473, 0.1649, 0.5741, 0.3429, 0.2616, 0.1776, 0.2784, 0.1268, 0.1987, 0.0857, 0.1405, 0.2199, 0.016, 0.0517, 0.0822, 0.0461)) ,
(77, 698.4565, 1, (0.9703, 0.2828, 0.8853, 0.7901, 1.0, 0.6872, 0.2561, 0.6743, 0.3603, 0.2284, 0.3726, 0.1408, 0.0767, 0.0655, 0.1344, 0.0987, 0.1835, 0.1671, 0.0997, 0.034)) ,
)

instruments=[]
instruments.append(sinusoids)
instruments.append(gaita_galega)
instruments.append(gaita_asturiana)
instruments.append(ghb)
instruments.append(uilleann)
instruments.append(sackpipa_detuned)


generated=[]
for instrument in instruments:
	samples=[]
	#print instrument[0]
	for note in instrument[1:]:
		freq=note[1]
		amplitude=note[2]
		total_samples=int(SAMPLE_RATE/freq)
		#sinusoid=[int((math.sin(2.0*math.pi*freq*(x/float(SAMPLE_RATE)))) for x in range(total_samples)]
		partials=[]
		for i,partial in enumerate(note[3]):
			partial_sinusoid=[(math.sin(2.0*math.pi*freq*(i+1)*(x/float(SAMPLE_RATE))))*partial for x in range((total_samples))]
			partials.append(partial_sinusoid)

		#MIX PARTIALS
		loop=[]
		for i in range(total_samples):
			value=0
			for item in partials:
				value+=item[i]
			loop.append(value)

		#NORMALIZE
		max_sample=max(max(loop),abs(min(loop)))
		#print max_sample
		if SIGNED==False:
			factor=((((2**BITS))/2)-1)/max_sample
		else:
			factor=((((2**BITS))/2)-1)/max_sample
		normalized_loop=[int(x*factor) for x in loop]
		#SCALE
		normalized_loop=[int(x*amplitude) for x in normalized_loop]

		#print max(normalized_loop)
		#print min(normalized_loop)
		if SIGNED==False:
			normalized_loop=[x+((((2**BITS))/2)-1) for x in normalized_loop]

		#print max(normalized_loop)
		#print min(normalized_loop)
		#sys.exit()

		sample_name="instrument_"+instrument[0]+"_note_"+str(note[0])
		sample=(sample_name, note[0], normalized_loop)
		samples.append(sample)
	generated.append((instrument[0], samples))


#print generated

output="""
// OPENPIPE SAMPLES
// FILE AUTOMATICALLY GENERATED USING samples.py
// DO NOT EDIT BY HAND

typedef struct{
  int16_t note;
  int16_t len;
  char* sample;
}sample_t;

typedef struct{
  char* name;
  sample_t* samples;
}instrument_t;

"""


if BITS>8:
	sample_type="int16_t"
else:
	sample_type="uint8_t"

for item in generated:
	#print item[0]
	for sample in item[1]:
		#print sample[0]
		output+="const %s %s [] PROGMEM = {" % (sample_type,sample[0])
		for value in sample[2]:
			output+=str(value)+","
		output+="};\r\n"

for item in generated:
	output += "\r\nconst sample_t instrument_%s_samples[]={\r\n" % item[0]
	for sample in item[1]:
		output+="\t{%i, %i, (char*)%s},\r\n" % (sample[1], len(sample[2]), sample[0])
	output += "\t{0xFF, 0,0} // END\r\n};"

output += "\r\n"

for i,item in enumerate(generated):
	#output+= "#define INSTRUMENT_%s %i\r\n" % (item[0], i)
	output+= "#define INSTRUMENT_%s (sample_t*)instrument_%s_samples\r\n" % (item[0], item[0])

'''
output += "\r\nconst instrument_t instruments[]={\r\n"
for item in generated:
	output+= "{(char*)\"%s\", (sample_t*)instrument_%s_samples},\r\n" % (item[0], item[0])
output += "};"
'''


print output

f = open('samples.h', 'w')
f.write(output)
f.close
