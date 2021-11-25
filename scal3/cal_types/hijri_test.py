import unittest
from scal3.cal_types import hijri

class TestHijri(unittest.TestCase):
	dateToJdDict = {
		(1426, 1, 1): 2453413,
		(1426, 2, 1): 2453443,
		(1426, 3, 1): 2453471,
		(1426, 4, 1): 2453501,
		(1426, 5, 1): 2453530,
		(1426, 6, 1): 2453560,
		(1426, 7, 1): 2453590,
		(1426, 8, 1): 2453620,
		(1426, 9, 1): 2453650,
		(1426, 10, 1): 2453679,
		(1426, 11, 1): 2453709,
		(1426, 12, 1): 2453738,
		(1427, 1, 1): 2453767,
		(1427, 2, 1): 2453797,
		(1427, 3, 1): 2453826,
		(1427, 4, 1): 2453855,
		(1427, 5, 1): 2453885,
		(1427, 6, 1): 2453914,
		(1427, 7, 1): 2453944,
		(1427, 8, 1): 2453974,
		(1427, 9, 1): 2454004,
		(1427, 10, 1): 2454034,
		(1427, 11, 1): 2454063,
		(1427, 12, 1): 2454092,
		(1428, 1, 1): 2454122,
		(1428, 2, 1): 2454151,
		(1428, 3, 1): 2454181,
		(1428, 4, 1): 2454210,
		(1428, 5, 1): 2454239,
		(1428, 6, 1): 2454268,
		(1428, 7, 1): 2454298,
		(1428, 8, 1): 2454328,
		(1428, 9, 1): 2454357,
		(1428, 10, 1): 2454387,
		(1428, 11, 1): 2454417,
		(1428, 12, 1): 2454447,
		(1429, 1, 1): 2454476,
		(1429, 2, 1): 2454506,
		(1429, 3, 1): 2454535,
		(1429, 4, 1): 2454565,
		(1429, 5, 1): 2454594,
		(1429, 6, 1): 2454623,
		(1429, 7, 1): 2454652,
		(1429, 8, 1): 2454682,
		(1429, 9, 1): 2454712,
		(1429, 10, 1): 2454741,
		(1429, 11, 1): 2454771,
		(1429, 12, 1): 2454801,
		(1430, 1, 1): 2454830,
		(1430, 2, 1): 2454860,
		(1430, 3, 1): 2454890,
		(1430, 4, 1): 2454919,
		(1430, 5, 1): 2454948,
		(1430, 6, 1): 2454978,
		(1430, 7, 1): 2455007,
		(1430, 8, 1): 2455037,
		(1430, 9, 1): 2455066,
		(1430, 10, 1): 2455095,
		(1430, 11, 1): 2455125,
		(1430, 12, 1): 2455155,
		(1431, 1, 1): 2455184,
		(1431, 2, 1): 2455214,
		(1431, 3, 1): 2455244,
		(1431, 4, 1): 2455273,
		(1431, 5, 1): 2455303,
		(1431, 6, 1): 2455332,
		(1431, 7, 1): 2455362,
		(1431, 8, 1): 2455391,
		(1431, 9, 1): 2455421,
		(1431, 10, 1): 2455450,
		(1431, 11, 1): 2455479,
		(1431, 12, 1): 2455509,
		(1432, 1, 1): 2455538,
		(1432, 2, 1): 2455568,
		(1432, 3, 1): 2455598,
		(1432, 4, 1): 2455627,
		(1432, 5, 1): 2455657,
		(1432, 6, 1): 2455687,
		(1432, 7, 1): 2455717,
		(1432, 8, 1): 2455746,
		(1432, 9, 1): 2455775,
		(1432, 10, 1): 2455805,
		(1432, 11, 1): 2455834,
		(1432, 12, 1): 2455864,
		(1433, 1, 1): 2455893,
		(1433, 2, 1): 2455922,
		(1433, 3, 1): 2455952,
		(1433, 4, 1): 2455981,
		(1433, 5, 1): 2456011,
		(1433, 6, 1): 2456041,
		(1433, 7, 1): 2456071,
		(1433, 8, 1): 2456100,
		(1433, 9, 1): 2456130,
		(1433, 10, 1): 2456159,
		(1433, 11, 1): 2456189,
		(1433, 12, 1): 2456218,
		(1434, 1, 1): 2456248,
		(1434, 2, 1): 2456277,
		(1434, 3, 1): 2456306,
		(1434, 4, 1): 2456336,
		(1434, 5, 1): 2456365,
		(1434, 6, 1): 2456395,
		(1434, 7, 1): 2456425,
		(1434, 8, 1): 2456454,
		(1434, 9, 1): 2456484,
		(1434, 10, 1): 2456514,
		(1434, 11, 1): 2456543,
		(1434, 12, 1): 2456573,
		(1435, 1, 1): 2456602,
		(1435, 2, 1): 2456631,
		(1435, 3, 1): 2456661,
		(1435, 4, 1): 2456690,
		(1435, 5, 1): 2456720,
		(1435, 6, 1): 2456749,
		(1435, 7, 1): 2456779,
		(1435, 8, 1): 2456808,
		(1435, 9, 1): 2456838,
		(1435, 10, 1): 2456868,
		(1435, 11, 1): 2456898,
		(1435, 12, 1): 2456927,
		(1436, 1, 1): 2456957,
		(1436, 2, 1): 2456986,
		(1436, 3, 1): 2457016,
		(1436, 4, 1): 2457045,
		(1436, 5, 1): 2457074,
		(1436, 6, 1): 2457104,
		(1436, 7, 1): 2457133,
		(1436, 8, 1): 2457163,
		(1436, 9, 1): 2457192,
		(1436, 10, 1): 2457222,
		(1436, 11, 1): 2457251,
		(1436, 12, 1): 2457281,
		(1437, 1, 1): 2457311,
		(1437, 2, 1): 2457340,
		(1437, 3, 1): 2457370,
		(1437, 4, 1): 2457400,
		(1437, 5, 1): 2457429,
		(1437, 6, 1): 2457459,
		(1437, 7, 1): 2457488,
		(1437, 8, 1): 2457517,
		(1437, 9, 1): 2457547,
		(1437, 10, 1): 2457576,
		(1437, 11, 1): 2457605,
		(1437, 12, 1): 2457635,
		(1438, 1, 1): 2457665,
		(1438, 2, 1): 2457694,
		(1438, 3, 1): 2457724,
		(1438, 4, 1): 2457754,
		(1438, 5, 1): 2457784,
		(1438, 6, 1): 2457813,
		(1438, 7, 1): 2457843,
		(1438, 8, 1): 2457872,
		(1438, 9, 1): 2457901,
		(1438, 10, 1): 2457931,
		(1438, 11, 1): 2457960,
		(1438, 12, 1): 2457989,
		(1439, 1, 1): 2458019,
		(1439, 2, 1): 2458048,
		(1439, 3, 1): 2458078,
		(1439, 4, 1): 2458108,
		(1439, 5, 1): 2458138,
		(1439, 6, 1): 2458168,
		(1439, 7, 1): 2458197,
		(1439, 8, 1): 2458227,
		(1439, 9, 1): 2458256,
		(1439, 10, 1): 2458285,
		(1439, 11, 1): 2458315,
		(1439, 12, 1): 2458344,
		(1440, 1, 1): 2458373,
		(1440, 2, 1): 2458403,
		(1440, 3, 1): 2458432,
		(1440, 4, 1): 2458462,
		(1440, 5, 1): 2458492,
		(1440, 6, 1): 2458522,
		(1440, 7, 1): 2458551,
		(1440, 8, 1): 2458581,
		(1440, 9, 1): 2458611,
		(1440, 10, 1): 2458640,
		(1440, 11, 1): 2458669,
		(1440, 12, 1): 2458699,
		(1441, 1, 1): 2458728,
		(1441, 2, 1): 2458757,
		(1441, 3, 1): 2458787,
		(1441, 4, 1): 2458816,
		(1441, 5, 1): 2458846,
		(1441, 6, 1): 2458876,
		(1441, 7, 1): 2458905,
		(1441, 8, 1): 2458935,
		(1441, 9, 1): 2458965,
		(1441, 10, 1): 2458994,
		(1441, 11, 1): 2459024,
		(1441, 12, 1): 2459053,
		(1442, 1, 1): 2459083,
		(1442, 2, 1): 2459112,
		(1442, 3, 1): 2459141,
		(1442, 4, 1): 2459171,
		(1442, 5, 1): 2459200,
		(1442, 6, 1): 2459230,
		(1442, 7, 1): 2459259,
		(1442, 8, 1): 2459289,
		(1442, 9, 1): 2459319,
		(1442, 10, 1): 2459348,
		(1442, 11, 1): 2459378,
		(1442, 12, 1): 2459408,
		(1443, 1, 1): 2459437,
		(1443, 2, 1): 2459466,
		(1443, 3, 1): 2459496,
		(1443, 4, 1): 2459526,
		(1443, 5, 1): 2459555,
		(1443, 6, 1): 2459584,
		(1443, 7, 1): 2459614,
		(1443, 8, 1): 2459643,
		(1443, 9, 1): 2459673,
		(1443, 10, 1): 2459702,
		(1443, 11, 1): 2459732,
		(1443, 12, 1): 2459762,
		(1444, 1, 1): 2459791,
		(1444, 2, 1): 2459821,
		(1444, 3, 1): 2459851,
		(1444, 4, 1): 2459880,
		(1444, 5, 1): 2459910,
		(1444, 6, 1): 2459939,
		(1444, 7, 1): 2459968,
		(1444, 8, 1): 2459998,
	}
	jdToDateDict = {
		2453442: (1426, 2, 1),
		2453469: (1426, 2, 28),
		2453496: (1426, 3, 26),
		2453523: (1426, 4, 23),
		2453550: (1426, 5, 21),
		2453577: (1426, 6, 18),
		2453604: (1426, 7, 15),
		2453631: (1426, 8, 12),
		2453658: (1426, 9, 9),
		2453685: (1426, 10, 7),
		2453712: (1426, 11, 4),
		2453739: (1426, 12, 2),
		2453766: (1426, 12, 29),
		2453793: (1427, 1, 27),
		2453820: (1427, 2, 24),
		2453847: (1427, 3, 22),
		2453874: (1427, 4, 20),
		2453901: (1427, 5, 17),
		2453928: (1427, 6, 15),
		2453955: (1427, 7, 12),
		2453982: (1427, 8, 9),
		2454009: (1427, 9, 6),
		2454036: (1427, 10, 3),
		2454063: (1427, 11, 1),
		2454090: (1427, 11, 28),
		2454117: (1427, 12, 26),
		2454144: (1428, 1, 23),
		2454171: (1428, 2, 21),
		2454198: (1428, 3, 18),
		2454225: (1428, 4, 16),
		2454252: (1428, 5, 14),
		2454279: (1428, 6, 12),
		2454306: (1428, 7, 9),
		2454333: (1428, 8, 6),
		2454360: (1428, 9, 4),
		2454387: (1428, 10, 1),
		2454414: (1428, 10, 28),
		2454441: (1428, 11, 25),
		2454468: (1428, 12, 22),
		2454495: (1429, 1, 20),
		2454522: (1429, 2, 17),
		2454549: (1429, 3, 15),
		2454576: (1429, 4, 12),
		2454603: (1429, 5, 10),
		2454630: (1429, 6, 8),
		2454657: (1429, 7, 6),
		2454684: (1429, 8, 3),
		2454711: (1429, 8, 30),
		2454738: (1429, 9, 27),
		2454765: (1429, 10, 25),
		2454792: (1429, 11, 22),
		2454819: (1429, 12, 19),
		2454846: (1430, 1, 17),
		2454873: (1430, 2, 14),
		2454900: (1430, 3, 11),
		2454927: (1430, 4, 9),
		2454954: (1430, 5, 7),
		2454981: (1430, 6, 4),
		2455008: (1430, 7, 2),
		2455035: (1430, 7, 29),
		2455062: (1430, 8, 26),
		2455089: (1430, 9, 24),
		2455116: (1430, 10, 22),
		2455143: (1430, 11, 19),
		2455170: (1430, 12, 16),
		2455197: (1431, 1, 14),
		2455224: (1431, 2, 11),
		2455251: (1431, 3, 8),
		2455278: (1431, 4, 6),
		2455305: (1431, 5, 3),
		2455332: (1431, 6, 1),
		2455359: (1431, 6, 28),
		2455386: (1431, 7, 25),
		2455413: (1431, 8, 23),
		2455440: (1431, 9, 20),
		2455467: (1431, 10, 18),
		2455494: (1431, 11, 16),
		2455521: (1431, 12, 13),
		2455548: (1432, 1, 11),
		2455575: (1432, 2, 8),
		2455602: (1432, 3, 5),
		2455629: (1432, 4, 3),
		2455656: (1432, 4, 30),
		2455683: (1432, 5, 27),
		2455710: (1432, 6, 24),
		2455737: (1432, 7, 21),
		2455764: (1432, 8, 19),
		2455791: (1432, 9, 17),
		2455818: (1432, 10, 14),
		2455845: (1432, 11, 12),
		2455872: (1432, 12, 9),
		2455899: (1433, 1, 7),
		2455926: (1433, 2, 5),
		2455953: (1433, 3, 2),
		2455980: (1433, 3, 29),
		2456007: (1433, 4, 27),
		2456034: (1433, 5, 24),
		2456061: (1433, 6, 21),
		2456088: (1433, 7, 18),
		2456115: (1433, 8, 16),
		2456142: (1433, 9, 13),
		2456169: (1433, 10, 11),
		2456196: (1433, 11, 8),
		2456223: (1433, 12, 6),
		2456250: (1434, 1, 3),
		2456277: (1434, 2, 1),
		2456304: (1434, 2, 28),
		2456331: (1434, 3, 26),
		2456358: (1434, 4, 23),
		2456385: (1434, 5, 21),
		2456412: (1434, 6, 18),
		2456439: (1434, 7, 15),
		2456466: (1434, 8, 13),
		2456493: (1434, 9, 10),
		2456520: (1434, 10, 7),
		2456547: (1434, 11, 5),
		2456574: (1434, 12, 2),
		2456601: (1434, 12, 29),
		2456628: (1435, 1, 27),
		2456655: (1435, 2, 25),
		2456682: (1435, 3, 22),
		2456709: (1435, 4, 20),
		2456736: (1435, 5, 17),
		2456763: (1435, 6, 15),
		2456790: (1435, 7, 12),
		2456817: (1435, 8, 10),
		2456844: (1435, 9, 7),
		2456871: (1435, 10, 4),
		2456898: (1435, 11, 1),
		2456925: (1435, 11, 28),
		2456952: (1435, 12, 26),
		2456979: (1436, 1, 23),
		2457006: (1436, 2, 21),
		2457033: (1436, 3, 18),
		2457060: (1436, 4, 16),
		2457087: (1436, 5, 14),
		2457114: (1436, 6, 11),
		2457141: (1436, 7, 9),
		2457168: (1436, 8, 6),
		2457195: (1436, 9, 4),
		2457222: (1436, 10, 1),
		2457249: (1436, 10, 28),
		2457276: (1436, 11, 26),
		2457303: (1436, 12, 23),
		2457330: (1437, 1, 20),
		2457357: (1437, 2, 18),
		2457384: (1437, 3, 15),
		2457411: (1437, 4, 12),
		2457438: (1437, 5, 10),
		2457465: (1437, 6, 7),
		2457492: (1437, 7, 5),
		2457519: (1437, 8, 3),
		2457546: (1437, 8, 30),
		2457573: (1437, 9, 27),
		2457600: (1437, 10, 25),
		2457627: (1437, 11, 23),
		2457654: (1437, 12, 20),
		2457681: (1438, 1, 17),
		2457708: (1438, 2, 15),
		2457735: (1438, 3, 12),
		2457762: (1438, 4, 9),
		2457789: (1438, 5, 6),
		2457816: (1438, 6, 4),
		2457843: (1438, 7, 1),
		2457870: (1438, 7, 28),
		2457897: (1438, 8, 26),
		2457924: (1438, 9, 24),
		2457951: (1438, 10, 21),
		2457978: (1438, 11, 19),
		2458005: (1438, 12, 17),
		2458032: (1439, 1, 14),
		2458059: (1439, 2, 12),
		2458086: (1439, 3, 9),
		2458113: (1439, 4, 6),
		2458140: (1439, 5, 3),
		2458167: (1439, 5, 30),
		2458194: (1439, 6, 27),
		2458221: (1439, 7, 25),
		2458248: (1439, 8, 22),
		2458275: (1439, 9, 20),
		2458302: (1439, 10, 18),
		2458329: (1439, 11, 15),
		2458356: (1439, 12, 13),
		2458383: (1440, 1, 11),
		2458410: (1440, 2, 8),
		2458437: (1440, 3, 6),
		2458464: (1440, 4, 3),
		2458491: (1440, 4, 30),
		2458518: (1440, 5, 27),
		2458545: (1440, 6, 24),
		2458572: (1440, 7, 22),
		2458599: (1440, 8, 19),
		2458626: (1440, 9, 16),
		2458653: (1440, 10, 14),
		2458680: (1440, 11, 12),
		2458707: (1440, 12, 9),
		2458734: (1441, 1, 7),
		2458761: (1441, 2, 5),
		2458788: (1441, 3, 2),
		2458815: (1441, 3, 29),
		2458842: (1441, 4, 27),
		2458869: (1441, 5, 24),
		2458896: (1441, 6, 21),
		2458923: (1441, 7, 19),
		2458950: (1441, 8, 16),
		2458977: (1441, 9, 13),
		2459004: (1441, 10, 11),
		2459031: (1441, 11, 8),
		2459058: (1441, 12, 6),
		2459085: (1442, 1, 3),
		2459112: (1442, 2, 1),
		2459139: (1442, 2, 28),
		2459166: (1442, 3, 26),
		2459193: (1442, 4, 23),
		2459220: (1442, 5, 21),
		2459247: (1442, 6, 18),
		2459274: (1442, 7, 16),
		2459301: (1442, 8, 13),
		2459328: (1442, 9, 10),
		2459355: (1442, 10, 8),
		2459382: (1442, 11, 5),
		2459409: (1442, 12, 2),
		2459436: (1442, 12, 29),
		2459463: (1443, 1, 27),
		2459490: (1443, 2, 25),
		2459517: (1443, 3, 22),
		2459544: (1443, 4, 19),
		2459571: (1443, 5, 17),
		2459598: (1443, 6, 15),
		2459625: (1443, 7, 12),

		2459660: (1443, 8, 18),
		2459691: (1443, 9, 19),
		2459722: (1443, 10, 21),
		2459753: (1443, 11, 22),
		2459784: (1443, 12, 23),
		2459815: (1444, 1, 25),
		2459846: (1444, 2, 26),
		2459876: (1444, 3, 26),
		2459906: (1444, 4, 27),
		2459936: (1444, 5, 27),
		2459966: (1444, 6, 28),
		2459996: (1444, 7, 29),
	}

	def test_to_jd(self):
		for date, jd in self.dateToJdDict.items():
			jdActual = hijri.to_jd(*date)
			self.assertEqual(
				jdActual,
				jd,
				f"date={date}, jd={jd}, jdActual={jdActual}",
			)

	def test_jd_to(self):
		for jd, date in self.jdToDateDict.items():
			dateActual = hijri.jd_to(jd)
			self.assertEqual(
				dateActual,
				date,
				f"jd={jd}, date={date}, dateActual={dateActual}",
			)

def print_to_jd_diff():
	for ym in hijri.monthDb.monthLenByYm:
		y, m = divmod(ym, 12)
		m += 1
		print(hijri.to_jd(y, m, 1) - hijri.to_jd_c(y, m, 1))

def gen_test_date_to_jd(golang=False):
	for year in range(1426, 1444):
		for month in range(1, 13):
			day = 1
			jd = hijri.to_jd(year, month, day)
			if golang:
				print(f"\t\tlib.NewDate({year}, {month}, {day}): {jd},")
				continue
			print(f"\t\t({year}, {month}, {day}): {jd},")

def gen_test_jd_to_date(golang=False):
	for jd in range(2453442, 2459660 + 30, 27):
		year, month, day = hijri.jd_to(jd)
		if golang:
			print(f"\t\t{jd}: lib.NewDate({year}, {month}, {day}),")
			continue
		print(f"\t\t{jd}: ({year}, {month}, {day}),")

if __name__ == "__main__":
	# print(f"startDate = {hijri.monthDb.startDate}")
	print(f"endJd = {hijri.monthDb.endJd}")
	# print("map[int]int" + repr(hijri.monthDb.monthLenByYm).replace(": ", ":"))
	# print_to_jd_diff()
	# gen_test_date_to_jd(golang=True)
	# gen_test_jd_to_date(golang=True)
	unittest.main()
