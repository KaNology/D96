# Generated from c:\Users\ADMIN\Desktop\assignment2\src\main\d96\parser\D96.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3B")
        buf.write("\u020f\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\3\2\6\2f\n\2\r\2\16")
        buf.write("\2g\3\2\3\2\3\3\3\3\3\3\3\3\5\3p\n\3\3\3\3\3\3\3\3\3\3")
        buf.write("\4\3\4\7\4x\n\4\f\4\16\4{\13\4\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\7\5\u0089\n\5\f\5\16\5\u008c")
        buf.write("\13\5\5\5\u008e\n\5\3\5\3\5\3\6\3\6\3\6\7\6\u0095\n\6")
        buf.write("\f\6\16\6\u0098\13\6\3\7\3\7\3\b\3\b\3\b\5\b\u009f\n\b")
        buf.write("\3\t\3\t\3\t\5\t\u00a4\n\t\3\t\3\t\3\t\3\t\3\t\5\t\u00ab")
        buf.write("\n\t\3\t\3\t\3\t\3\t\5\t\u00b1\n\t\3\t\3\t\3\n\3\n\3\n")
        buf.write("\7\n\u00b8\n\n\f\n\16\n\u00bb\13\n\3\13\3\13\3\13\3\13")
        buf.write("\3\f\3\f\3\f\7\f\u00c4\n\f\f\f\16\f\u00c7\13\f\3\r\3\r")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\5\17\u00d4")
        buf.write("\n\17\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\5\21\u00e1\n\21\3\22\3\22\3\22\3\22\3\22\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\22\7\22\u00ee\n\22\f\22\16\22\u00f1")
        buf.write("\13\22\5\22\u00f3\n\22\3\22\3\22\3\23\3\23\3\23\7\23\u00fa")
        buf.write("\n\23\f\23\16\23\u00fd\13\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\5\25\u0106\n\25\3\26\3\26\3\26\3\26\3\26\3")
        buf.write("\26\3\26\3\26\5\26\u0110\n\26\3\27\3\27\3\27\3\27\3\27")
        buf.write("\6\27\u0117\n\27\r\27\16\27\u0118\3\30\3\30\3\30\3\30")
        buf.write("\7\30\u011f\n\30\f\30\16\30\u0122\13\30\3\30\3\30\5\30")
        buf.write("\u0126\n\30\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3")
        buf.write("\32\3\32\3\32\3\32\3\32\3\32\5\32\u0136\n\32\3\32\3\32")
        buf.write("\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35\5\35\u0143")
        buf.write("\n\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\5\36\u014c\n")
        buf.write("\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\5\37\u0156")
        buf.write("\n\37\3\37\3\37\3\37\3 \3 \3 \7 \u015e\n \f \16 \u0161")
        buf.write("\13 \3 \3 \3!\3!\3!\3!\3!\3!\7!\u016b\n!\f!\16!\u016e")
        buf.write("\13!\3\"\3\"\3\"\3\"\3\"\3\"\7\"\u0176\n\"\f\"\16\"\u0179")
        buf.write("\13\"\3#\3#\3#\3#\3#\3#\7#\u0181\n#\f#\16#\u0184\13#\3")
        buf.write("$\3$\3$\3$\3$\3$\7$\u018c\n$\f$\16$\u018f\13$\3%\3%\3")
        buf.write("%\3%\3%\3%\7%\u0197\n%\f%\16%\u019a\13%\3&\3&\3&\5&\u019f")
        buf.write("\n&\3\'\3\'\3\'\5\'\u01a4\n\'\3(\3(\3(\3(\3(\3(\3(\3(")
        buf.write("\6(\u01ae\n(\r(\16(\u01af\7(\u01b2\n(\f(\16(\u01b5\13")
        buf.write("(\3)\3)\3)\3)\3)\3)\3)\3)\5)\u01bf\n)\3)\5)\u01c2\n)\7")
        buf.write(")\u01c4\n)\f)\16)\u01c7\13)\3*\3*\3*\3*\3*\5*\u01ce\n")
        buf.write("*\3*\5*\u01d1\n*\3*\5*\u01d4\n*\3+\3+\3+\3+\5+\u01da\n")
        buf.write("+\3+\3+\5+\u01de\n+\3,\3,\3,\3,\3,\5,\u01e5\n,\3-\3-\3")
        buf.write("-\7-\u01ea\n-\f-\16-\u01ed\13-\3.\3.\3.\3.\3.\3.\3.\3")
        buf.write(".\3.\5.\u01f8\n.\3/\3/\3/\5/\u01fd\n/\3/\3/\3\60\3\60")
        buf.write("\3\60\7\60\u0204\n\60\f\60\16\60\u0207\13\60\3\61\3\61")
        buf.write("\5\61\u020b\n\61\3\62\3\62\3\62\2\t@BDFHNP\63\2\4\6\b")
        buf.write("\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668")
        buf.write(":<>@BDFHJLNPRTVXZ\\^`b\2\13\3\2\24\25\3\2<=\3\2\r\20\3")
        buf.write("\2\64\65\4\2--/\63\3\2+,\3\2%&\3\2\')\3\2\t\n\2\u0222")
        buf.write("\2e\3\2\2\2\4k\3\2\2\2\6y\3\2\2\2\b|\3\2\2\2\n\u0091\3")
        buf.write("\2\2\2\f\u0099\3\2\2\2\16\u009e\3\2\2\2\20\u00b0\3\2\2")
        buf.write("\2\22\u00b4\3\2\2\2\24\u00bc\3\2\2\2\26\u00c0\3\2\2\2")
        buf.write("\30\u00c8\3\2\2\2\32\u00ca\3\2\2\2\34\u00d3\3\2\2\2\36")
        buf.write("\u00d5\3\2\2\2 \u00e0\3\2\2\2\"\u00e2\3\2\2\2$\u00f6\3")
        buf.write("\2\2\2&\u00fe\3\2\2\2(\u0105\3\2\2\2*\u010f\3\2\2\2,\u0111")
        buf.write("\3\2\2\2.\u011a\3\2\2\2\60\u0127\3\2\2\2\62\u012c\3\2")
        buf.write("\2\2\64\u013a\3\2\2\2\66\u013d\3\2\2\28\u0140\3\2\2\2")
        buf.write(":\u0146\3\2\2\2<\u0150\3\2\2\2>\u015a\3\2\2\2@\u0164\3")
        buf.write("\2\2\2B\u016f\3\2\2\2D\u017a\3\2\2\2F\u0185\3\2\2\2H\u0190")
        buf.write("\3\2\2\2J\u019e\3\2\2\2L\u01a3\3\2\2\2N\u01a5\3\2\2\2")
        buf.write("P\u01b6\3\2\2\2R\u01d3\3\2\2\2T\u01dd\3\2\2\2V\u01e4\3")
        buf.write("\2\2\2X\u01e6\3\2\2\2Z\u01f7\3\2\2\2\\\u01f9\3\2\2\2^")
        buf.write("\u0200\3\2\2\2`\u020a\3\2\2\2b\u020c\3\2\2\2df\5\4\3\2")
        buf.write("ed\3\2\2\2fg\3\2\2\2ge\3\2\2\2gh\3\2\2\2hi\3\2\2\2ij\7")
        buf.write("\2\2\3j\3\3\2\2\2kl\7\23\2\2lo\7<\2\2mn\7$\2\2np\7<\2")
        buf.write("\2om\3\2\2\2op\3\2\2\2pq\3\2\2\2qr\7\"\2\2rs\5\6\4\2s")
        buf.write("t\7#\2\2t\5\3\2\2\2ux\5\b\5\2vx\5\20\t\2wu\3\2\2\2wv\3")
        buf.write("\2\2\2x{\3\2\2\2yw\3\2\2\2yz\3\2\2\2z\7\3\2\2\2{y\3\2")
        buf.write("\2\2|}\t\2\2\2}~\5\n\6\2~\177\7$\2\2\177\u008d\5\16\b")
        buf.write("\2\u0080\u0081\7.\2\2\u0081\u008a\5@!\2\u0082\u0083\6")
        buf.write("\5\2\3\u0083\u0084\7 \2\2\u0084\u0085\5@!\2\u0085\u0086")
        buf.write("\3\2\2\2\u0086\u0087\b\5\1\2\u0087\u0089\3\2\2\2\u0088")
        buf.write("\u0082\3\2\2\2\u0089\u008c\3\2\2\2\u008a\u0088\3\2\2\2")
        buf.write("\u008a\u008b\3\2\2\2\u008b\u008e\3\2\2\2\u008c\u008a\3")
        buf.write("\2\2\2\u008d\u0080\3\2\2\2\u008d\u008e\3\2\2\2\u008e\u008f")
        buf.write("\3\2\2\2\u008f\u0090\7!\2\2\u0090\t\3\2\2\2\u0091\u0096")
        buf.write("\5\f\7\2\u0092\u0093\7 \2\2\u0093\u0095\5\f\7\2\u0094")
        buf.write("\u0092\3\2\2\2\u0095\u0098\3\2\2\2\u0096\u0094\3\2\2\2")
        buf.write("\u0096\u0097\3\2\2\2\u0097\13\3\2\2\2\u0098\u0096\3\2")
        buf.write("\2\2\u0099\u009a\t\3\2\2\u009a\r\3\2\2\2\u009b\u009f\5")
        buf.write("\30\r\2\u009c\u009f\5\32\16\2\u009d\u009f\5\36\20\2\u009e")
        buf.write("\u009b\3\2\2\2\u009e\u009c\3\2\2\2\u009e\u009d\3\2\2\2")
        buf.write("\u009f\17\3\2\2\2\u00a0\u00a1\5\f\7\2\u00a1\u00a3\7\33")
        buf.write("\2\2\u00a2\u00a4\5\22\n\2\u00a3\u00a2\3\2\2\2\u00a3\u00a4")
        buf.write("\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5\u00a6\7\34\2\2\u00a6")
        buf.write("\u00b1\3\2\2\2\u00a7\u00a8\7\27\2\2\u00a8\u00aa\7\33\2")
        buf.write("\2\u00a9\u00ab\5\22\n\2\u00aa\u00a9\3\2\2\2\u00aa\u00ab")
        buf.write("\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac\u00b1\7\34\2\2\u00ad")
        buf.write("\u00ae\7\30\2\2\u00ae\u00af\7\33\2\2\u00af\u00b1\7\34")
        buf.write("\2\2\u00b0\u00a0\3\2\2\2\u00b0\u00a7\3\2\2\2\u00b0\u00ad")
        buf.write("\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00b3\5> \2\u00b3\21")
        buf.write("\3\2\2\2\u00b4\u00b9\5\24\13\2\u00b5\u00b6\7!\2\2\u00b6")
        buf.write("\u00b8\5\24\13\2\u00b7\u00b5\3\2\2\2\u00b8\u00bb\3\2\2")
        buf.write("\2\u00b9\u00b7\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\23\3")
        buf.write("\2\2\2\u00bb\u00b9\3\2\2\2\u00bc\u00bd\5\26\f\2\u00bd")
        buf.write("\u00be\7$\2\2\u00be\u00bf\5\16\b\2\u00bf\25\3\2\2\2\u00c0")
        buf.write("\u00c5\7<\2\2\u00c1\u00c2\7 \2\2\u00c2\u00c4\7<\2\2\u00c3")
        buf.write("\u00c1\3\2\2\2\u00c4\u00c7\3\2\2\2\u00c5\u00c3\3\2\2\2")
        buf.write("\u00c5\u00c6\3\2\2\2\u00c6\27\3\2\2\2\u00c7\u00c5\3\2")
        buf.write("\2\2\u00c8\u00c9\t\4\2\2\u00c9\31\3\2\2\2\u00ca\u00cb")
        buf.write("\7\13\2\2\u00cb\u00cc\7\35\2\2\u00cc\u00cd\5\34\17\2\u00cd")
        buf.write("\u00ce\7 \2\2\u00ce\u00cf\79\2\2\u00cf\u00d0\7\36\2\2")
        buf.write("\u00d0\33\3\2\2\2\u00d1\u00d4\5\30\r\2\u00d2\u00d4\5\32")
        buf.write("\16\2\u00d3\u00d1\3\2\2\2\u00d3\u00d2\3\2\2\2\u00d4\35")
        buf.write("\3\2\2\2\u00d5\u00d6\7<\2\2\u00d6\37\3\2\2\2\u00d7\u00e1")
        buf.write("\5&\24\2\u00d8\u00e1\5.\30\2\u00d9\u00e1\5\62\32\2\u00da")
        buf.write("\u00e1\5\64\33\2\u00db\u00e1\5\66\34\2\u00dc\u00e1\58")
        buf.write("\35\2\u00dd\u00e1\5:\36\2\u00de\u00e1\5<\37\2\u00df\u00e1")
        buf.write("\5> \2\u00e0\u00d7\3\2\2\2\u00e0\u00d8\3\2\2\2\u00e0\u00d9")
        buf.write("\3\2\2\2\u00e0\u00da\3\2\2\2\u00e0\u00db\3\2\2\2\u00e0")
        buf.write("\u00dc\3\2\2\2\u00e0\u00dd\3\2\2\2\u00e0\u00de\3\2\2\2")
        buf.write("\u00e0\u00df\3\2\2\2\u00e1!\3\2\2\2\u00e2\u00e3\t\2\2")
        buf.write("\2\u00e3\u00e4\5$\23\2\u00e4\u00e5\7$\2\2\u00e5\u00f2")
        buf.write("\5\16\b\2\u00e6\u00e7\7.\2\2\u00e7\u00ef\5@!\2\u00e8\u00e9")
        buf.write("\6\22\3\3\u00e9\u00ea\7 \2\2\u00ea\u00eb\5@!\2\u00eb\u00ec")
        buf.write("\b\22\1\2\u00ec\u00ee\3\2\2\2\u00ed\u00e8\3\2\2\2\u00ee")
        buf.write("\u00f1\3\2\2\2\u00ef\u00ed\3\2\2\2\u00ef\u00f0\3\2\2\2")
        buf.write("\u00f0\u00f3\3\2\2\2\u00f1\u00ef\3\2\2\2\u00f2\u00e6\3")
        buf.write("\2\2\2\u00f2\u00f3\3\2\2\2\u00f3\u00f4\3\2\2\2\u00f4\u00f5")
        buf.write("\7!\2\2\u00f5#\3\2\2\2\u00f6\u00fb\7<\2\2\u00f7\u00f8")
        buf.write("\7 \2\2\u00f8\u00fa\7<\2\2\u00f9\u00f7\3\2\2\2\u00fa\u00fd")
        buf.write("\3\2\2\2\u00fb\u00f9\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc")
        buf.write("%\3\2\2\2\u00fd\u00fb\3\2\2\2\u00fe\u00ff\5(\25\2\u00ff")
        buf.write("\u0100\7.\2\2\u0100\u0101\5@!\2\u0101\u0102\7!\2\2\u0102")
        buf.write("\'\3\2\2\2\u0103\u0106\5,\27\2\u0104\u0106\5*\26\2\u0105")
        buf.write("\u0103\3\2\2\2\u0105\u0104\3\2\2\2\u0106)\3\2\2\2\u0107")
        buf.write("\u0108\5@!\2\u0108\u0109\7\37\2\2\u0109\u010a\7<\2\2\u010a")
        buf.write("\u0110\3\2\2\2\u010b\u010c\7<\2\2\u010c\u010d\7\66\2\2")
        buf.write("\u010d\u0110\7=\2\2\u010e\u0110\7<\2\2\u010f\u0107\3\2")
        buf.write("\2\2\u010f\u010b\3\2\2\2\u010f\u010e\3\2\2\2\u0110+\3")
        buf.write("\2\2\2\u0111\u0116\7<\2\2\u0112\u0113\7\35\2\2\u0113\u0114")
        buf.write("\5@!\2\u0114\u0115\7\36\2\2\u0115\u0117\3\2\2\2\u0116")
        buf.write("\u0112\3\2\2\2\u0117\u0118\3\2\2\2\u0118\u0116\3\2\2\2")
        buf.write("\u0118\u0119\3\2\2\2\u0119-\3\2\2\2\u011a\u011b\7\5\2")
        buf.write("\2\u011b\u0120\5\60\31\2\u011c\u011d\7\6\2\2\u011d\u011f")
        buf.write("\5\60\31\2\u011e\u011c\3\2\2\2\u011f\u0122\3\2\2\2\u0120")
        buf.write("\u011e\3\2\2\2\u0120\u0121\3\2\2\2\u0121\u0125\3\2\2\2")
        buf.write("\u0122\u0120\3\2\2\2\u0123\u0124\7\7\2\2\u0124\u0126\5")
        buf.write("> \2\u0125\u0123\3\2\2\2\u0125\u0126\3\2\2\2\u0126/\3")
        buf.write("\2\2\2\u0127\u0128\7\33\2\2\u0128\u0129\5@!\2\u0129\u012a")
        buf.write("\7\34\2\2\u012a\u012b\5> \2\u012b\61\3\2\2\2\u012c\u012d")
        buf.write("\7\b\2\2\u012d\u012e\7\33\2\2\u012e\u012f\5*\26\2\u012f")
        buf.write("\u0130\7\f\2\2\u0130\u0131\5@!\2\u0131\u0132\7\67\2\2")
        buf.write("\u0132\u0135\5@!\2\u0133\u0134\7\32\2\2\u0134\u0136\5")
        buf.write("@!\2\u0135\u0133\3\2\2\2\u0135\u0136\3\2\2\2\u0136\u0137")
        buf.write("\3\2\2\2\u0137\u0138\7\34\2\2\u0138\u0139\5> \2\u0139")
        buf.write("\63\3\2\2\2\u013a\u013b\7\3\2\2\u013b\u013c\7!\2\2\u013c")
        buf.write("\65\3\2\2\2\u013d\u013e\7\4\2\2\u013e\u013f\7!\2\2\u013f")
        buf.write("\67\3\2\2\2\u0140\u0142\7\21\2\2\u0141\u0143\5@!\2\u0142")
        buf.write("\u0141\3\2\2\2\u0142\u0143\3\2\2\2\u0143\u0144\3\2\2\2")
        buf.write("\u0144\u0145\7!\2\2\u01459\3\2\2\2\u0146\u0147\5@!\2\u0147")
        buf.write("\u0148\7\37\2\2\u0148\u0149\7<\2\2\u0149\u014b\7\33\2")
        buf.write("\2\u014a\u014c\5X-\2\u014b\u014a\3\2\2\2\u014b\u014c\3")
        buf.write("\2\2\2\u014c\u014d\3\2\2\2\u014d\u014e\7\34\2\2\u014e")
        buf.write("\u014f\7!\2\2\u014f;\3\2\2\2\u0150\u0151\7<\2\2\u0151")
        buf.write("\u0152\7\66\2\2\u0152\u0153\7=\2\2\u0153\u0155\7\33\2")
        buf.write("\2\u0154\u0156\5X-\2\u0155\u0154\3\2\2\2\u0155\u0156\3")
        buf.write("\2\2\2\u0156\u0157\3\2\2\2\u0157\u0158\7\34\2\2\u0158")
        buf.write("\u0159\7!\2\2\u0159=\3\2\2\2\u015a\u015f\7\"\2\2\u015b")
        buf.write("\u015e\5\"\22\2\u015c\u015e\5 \21\2\u015d\u015b\3\2\2")
        buf.write("\2\u015d\u015c\3\2\2\2\u015e\u0161\3\2\2\2\u015f\u015d")
        buf.write("\3\2\2\2\u015f\u0160\3\2\2\2\u0160\u0162\3\2\2\2\u0161")
        buf.write("\u015f\3\2\2\2\u0162\u0163\7#\2\2\u0163?\3\2\2\2\u0164")
        buf.write("\u0165\b!\1\2\u0165\u0166\5B\"\2\u0166\u016c\3\2\2\2\u0167")
        buf.write("\u0168\f\4\2\2\u0168\u0169\t\5\2\2\u0169\u016b\5@!\5\u016a")
        buf.write("\u0167\3\2\2\2\u016b\u016e\3\2\2\2\u016c\u016a\3\2\2\2")
        buf.write("\u016c\u016d\3\2\2\2\u016dA\3\2\2\2\u016e\u016c\3\2\2")
        buf.write("\2\u016f\u0170\b\"\1\2\u0170\u0171\5D#\2\u0171\u0177\3")
        buf.write("\2\2\2\u0172\u0173\f\4\2\2\u0173\u0174\t\6\2\2\u0174\u0176")
        buf.write("\5B\"\5\u0175\u0172\3\2\2\2\u0176\u0179\3\2\2\2\u0177")
        buf.write("\u0175\3\2\2\2\u0177\u0178\3\2\2\2\u0178C\3\2\2\2\u0179")
        buf.write("\u0177\3\2\2\2\u017a\u017b\b#\1\2\u017b\u017c\5F$\2\u017c")
        buf.write("\u0182\3\2\2\2\u017d\u017e\f\4\2\2\u017e\u017f\t\7\2\2")
        buf.write("\u017f\u0181\5F$\2\u0180\u017d\3\2\2\2\u0181\u0184\3\2")
        buf.write("\2\2\u0182\u0180\3\2\2\2\u0182\u0183\3\2\2\2\u0183E\3")
        buf.write("\2\2\2\u0184\u0182\3\2\2\2\u0185\u0186\b$\1\2\u0186\u0187")
        buf.write("\5H%\2\u0187\u018d\3\2\2\2\u0188\u0189\f\4\2\2\u0189\u018a")
        buf.write("\t\b\2\2\u018a\u018c\5H%\2\u018b\u0188\3\2\2\2\u018c\u018f")
        buf.write("\3\2\2\2\u018d\u018b\3\2\2\2\u018d\u018e\3\2\2\2\u018e")
        buf.write("G\3\2\2\2\u018f\u018d\3\2\2\2\u0190\u0191\b%\1\2\u0191")
        buf.write("\u0192\5J&\2\u0192\u0198\3\2\2\2\u0193\u0194\f\4\2\2\u0194")
        buf.write("\u0195\t\t\2\2\u0195\u0197\5J&\2\u0196\u0193\3\2\2\2\u0197")
        buf.write("\u019a\3\2\2\2\u0198\u0196\3\2\2\2\u0198\u0199\3\2\2\2")
        buf.write("\u0199I\3\2\2\2\u019a\u0198\3\2\2\2\u019b\u019c\7*\2\2")
        buf.write("\u019c\u019f\5J&\2\u019d\u019f\5L\'\2\u019e\u019b\3\2")
        buf.write("\2\2\u019e\u019d\3\2\2\2\u019fK\3\2\2\2\u01a0\u01a1\7")
        buf.write("&\2\2\u01a1\u01a4\5L\'\2\u01a2\u01a4\5N(\2\u01a3\u01a0")
        buf.write("\3\2\2\2\u01a3\u01a2\3\2\2\2\u01a4M\3\2\2\2\u01a5\u01a6")
        buf.write("\b(\1\2\u01a6\u01a7\5P)\2\u01a7\u01b3\3\2\2\2\u01a8\u01ad")
        buf.write("\f\4\2\2\u01a9\u01aa\7\35\2\2\u01aa\u01ab\5@!\2\u01ab")
        buf.write("\u01ac\7\36\2\2\u01ac\u01ae\3\2\2\2\u01ad\u01a9\3\2\2")
        buf.write("\2\u01ae\u01af\3\2\2\2\u01af\u01ad\3\2\2\2\u01af\u01b0")
        buf.write("\3\2\2\2\u01b0\u01b2\3\2\2\2\u01b1\u01a8\3\2\2\2\u01b2")
        buf.write("\u01b5\3\2\2\2\u01b3\u01b1\3\2\2\2\u01b3\u01b4\3\2\2\2")
        buf.write("\u01b4O\3\2\2\2\u01b5\u01b3\3\2\2\2\u01b6\u01b7\b)\1\2")
        buf.write("\u01b7\u01b8\5R*\2\u01b8\u01c5\3\2\2\2\u01b9\u01ba\f\4")
        buf.write("\2\2\u01ba\u01bb\7\37\2\2\u01bb\u01c1\7<\2\2\u01bc\u01be")
        buf.write("\7\33\2\2\u01bd\u01bf\5X-\2\u01be\u01bd\3\2\2\2\u01be")
        buf.write("\u01bf\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0\u01c2\7\34\2")
        buf.write("\2\u01c1\u01bc\3\2\2\2\u01c1\u01c2\3\2\2\2\u01c2\u01c4")
        buf.write("\3\2\2\2\u01c3\u01b9\3\2\2\2\u01c4\u01c7\3\2\2\2\u01c5")
        buf.write("\u01c3\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6Q\3\2\2\2\u01c7")
        buf.write("\u01c5\3\2\2\2\u01c8\u01c9\7<\2\2\u01c9\u01ca\7\66\2\2")
        buf.write("\u01ca\u01d0\7=\2\2\u01cb\u01cd\7\33\2\2\u01cc\u01ce\5")
        buf.write("X-\2\u01cd\u01cc\3\2\2\2\u01cd\u01ce\3\2\2\2\u01ce\u01cf")
        buf.write("\3\2\2\2\u01cf\u01d1\7\34\2\2\u01d0\u01cb\3\2\2\2\u01d0")
        buf.write("\u01d1\3\2\2\2\u01d1\u01d4\3\2\2\2\u01d2\u01d4\5T+\2\u01d3")
        buf.write("\u01c8\3\2\2\2\u01d3\u01d2\3\2\2\2\u01d4S\3\2\2\2\u01d5")
        buf.write("\u01d6\7\31\2\2\u01d6\u01d7\7<\2\2\u01d7\u01d9\7\33\2")
        buf.write("\2\u01d8\u01da\5X-\2\u01d9\u01d8\3\2\2\2\u01d9\u01da\3")
        buf.write("\2\2\2\u01da\u01db\3\2\2\2\u01db\u01de\7\34\2\2\u01dc")
        buf.write("\u01de\5V,\2\u01dd\u01d5\3\2\2\2\u01dd\u01dc\3\2\2\2\u01de")
        buf.write("U\3\2\2\2\u01df\u01e0\7\33\2\2\u01e0\u01e1\5@!\2\u01e1")
        buf.write("\u01e2\7\34\2\2\u01e2\u01e5\3\2\2\2\u01e3\u01e5\5Z.\2")
        buf.write("\u01e4\u01df\3\2\2\2\u01e4\u01e3\3\2\2\2\u01e5W\3\2\2")
        buf.write("\2\u01e6\u01eb\5@!\2\u01e7\u01e8\7 \2\2\u01e8\u01ea\5")
        buf.write("@!\2\u01e9\u01e7\3\2\2\2\u01ea\u01ed\3\2\2\2\u01eb\u01e9")
        buf.write("\3\2\2\2\u01eb\u01ec\3\2\2\2\u01ecY\3\2\2\2\u01ed\u01eb")
        buf.write("\3\2\2\2\u01ee\u01f8\7<\2\2\u01ef\u01f8\78\2\2\u01f0\u01f8")
        buf.write("\79\2\2\u01f1\u01f8\7:\2\2\u01f2\u01f8\7;\2\2\u01f3\u01f8")
        buf.write("\5b\62\2\u01f4\u01f8\5\\/\2\u01f5\u01f8\7\26\2\2\u01f6")
        buf.write("\u01f8\7\22\2\2\u01f7\u01ee\3\2\2\2\u01f7\u01ef\3\2\2")
        buf.write("\2\u01f7\u01f0\3\2\2\2\u01f7\u01f1\3\2\2\2\u01f7\u01f2")
        buf.write("\3\2\2\2\u01f7\u01f3\3\2\2\2\u01f7\u01f4\3\2\2\2\u01f7")
        buf.write("\u01f5\3\2\2\2\u01f7\u01f6\3\2\2\2\u01f8[\3\2\2\2\u01f9")
        buf.write("\u01fa\7\13\2\2\u01fa\u01fc\7\33\2\2\u01fb\u01fd\5^\60")
        buf.write("\2\u01fc\u01fb\3\2\2\2\u01fc\u01fd\3\2\2\2\u01fd\u01fe")
        buf.write("\3\2\2\2\u01fe\u01ff\7\34\2\2\u01ff]\3\2\2\2\u0200\u0205")
        buf.write("\5`\61\2\u0201\u0202\7 \2\2\u0202\u0204\5`\61\2\u0203")
        buf.write("\u0201\3\2\2\2\u0204\u0207\3\2\2\2\u0205\u0203\3\2\2\2")
        buf.write("\u0205\u0206\3\2\2\2\u0206_\3\2\2\2\u0207\u0205\3\2\2")
        buf.write("\2\u0208\u020b\5@!\2\u0209\u020b\5\\/\2\u020a\u0208\3")
        buf.write("\2\2\2\u020a\u0209\3\2\2\2\u020ba\3\2\2\2\u020c\u020d")
        buf.write("\t\n\2\2\u020dc\3\2\2\2\66gowy\u008a\u008d\u0096\u009e")
        buf.write("\u00a3\u00aa\u00b0\u00b9\u00c5\u00d3\u00e0\u00ef\u00f2")
        buf.write("\u00fb\u0105\u010f\u0118\u0120\u0125\u0135\u0142\u014b")
        buf.write("\u0155\u015d\u015f\u016c\u0177\u0182\u018d\u0198\u019e")
        buf.write("\u01a3\u01af\u01b3\u01be\u01c1\u01c5\u01cd\u01d0\u01d3")
        buf.write("\u01d9\u01dd\u01e4\u01eb\u01f7\u01fc\u0205\u020a")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Break'", "'Continue'", "'If'", "'Elseif'", 
                     "'Else'", "'Foreach'", "'True'", "'False'", "'Array'", 
                     "'In'", "'Int'", "'Float'", "'Boolean'", "'String'", 
                     "'Return'", "'Null'", "'Class'", "'Val'", "'Var'", 
                     "'Self'", "'Constructor'", "'Destructor'", "'New'", 
                     "'By'", "'('", "')'", "'['", "']'", "'.'", "','", "';'", 
                     "'{'", "'}'", "':'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'!'", "'&&'", "'||'", "'=='", "'='", "'!='", "'>'", 
                     "'>='", "'<'", "'<='", "'==.'", "'+.'", "'::'", "'..'" ]

    symbolicNames = [ "<INVALID>", "BREAK", "CONTINUE", "IF", "ELSEIF", 
                      "ELSE", "FOREACH", "TRUE", "FALSE", "ARRAY", "IN", 
                      "INT", "FLOAT", "BOOLEAN", "STRING", "RETURN", "NULL", 
                      "CLASS", "VAL", "VAR", "SELF", "CONSTRUCTOR", "DESTRUCTOR", 
                      "NEW", "BY", "LB", "RB", "LS", "RS", "DOT", "COMMA", 
                      "SEMI", "LP", "RP", "COLON", "ADD", "MINUS", "MUL", 
                      "DIV", "MOD", "NOT", "AND", "OR", "EQUAL", "ASSIGN", 
                      "DIFF", "GT", "GTE", "LT", "LTE", "STREQ", "STRADD", 
                      "DOUBLECOLON", "DOUBLEDOT", "ZERO", "INTLIT", "FLOATLIT", 
                      "STRINGLIT", "ID", "DOLLAR_ID", "COMMENT", "WS", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_classDeclaration = 1
    RULE_classBody = 2
    RULE_attrDeclaration = 3
    RULE_attrList = 4
    RULE_identifier = 5
    RULE_typeName = 6
    RULE_methodDeclaration = 7
    RULE_paraList = 8
    RULE_paraDeclaration = 9
    RULE_idList = 10
    RULE_primitiveType = 11
    RULE_arrayType = 12
    RULE_elementType = 13
    RULE_classType = 14
    RULE_stmt = 15
    RULE_declarationStmt = 16
    RULE_varList = 17
    RULE_assignStmt = 18
    RULE_assignLHS = 19
    RULE_scalar = 20
    RULE_indexOperation = 21
    RULE_ifStmt = 22
    RULE_ifBody = 23
    RULE_forInStmt = 24
    RULE_breakStmt = 25
    RULE_continueStmt = 26
    RULE_returnStmt = 27
    RULE_instanceCall = 28
    RULE_staticCall = 29
    RULE_blockStmt = 30
    RULE_exp = 31
    RULE_exp1 = 32
    RULE_exp2 = 33
    RULE_exp3 = 34
    RULE_exp4 = 35
    RULE_exp5 = 36
    RULE_exp6 = 37
    RULE_exp7 = 38
    RULE_exp8 = 39
    RULE_exp9 = 40
    RULE_exp10 = 41
    RULE_exp11 = 42
    RULE_expList = 43
    RULE_operand = 44
    RULE_indexArray = 45
    RULE_arrayBody = 46
    RULE_arrayLit = 47
    RULE_booleanLit = 48

    ruleNames =  [ "program", "classDeclaration", "classBody", "attrDeclaration", 
                   "attrList", "identifier", "typeName", "methodDeclaration", 
                   "paraList", "paraDeclaration", "idList", "primitiveType", 
                   "arrayType", "elementType", "classType", "stmt", "declarationStmt", 
                   "varList", "assignStmt", "assignLHS", "scalar", "indexOperation", 
                   "ifStmt", "ifBody", "forInStmt", "breakStmt", "continueStmt", 
                   "returnStmt", "instanceCall", "staticCall", "blockStmt", 
                   "exp", "exp1", "exp2", "exp3", "exp4", "exp5", "exp6", 
                   "exp7", "exp8", "exp9", "exp10", "exp11", "expList", 
                   "operand", "indexArray", "arrayBody", "arrayLit", "booleanLit" ]

    EOF = Token.EOF
    BREAK=1
    CONTINUE=2
    IF=3
    ELSEIF=4
    ELSE=5
    FOREACH=6
    TRUE=7
    FALSE=8
    ARRAY=9
    IN=10
    INT=11
    FLOAT=12
    BOOLEAN=13
    STRING=14
    RETURN=15
    NULL=16
    CLASS=17
    VAL=18
    VAR=19
    SELF=20
    CONSTRUCTOR=21
    DESTRUCTOR=22
    NEW=23
    BY=24
    LB=25
    RB=26
    LS=27
    RS=28
    DOT=29
    COMMA=30
    SEMI=31
    LP=32
    RP=33
    COLON=34
    ADD=35
    MINUS=36
    MUL=37
    DIV=38
    MOD=39
    NOT=40
    AND=41
    OR=42
    EQUAL=43
    ASSIGN=44
    DIFF=45
    GT=46
    GTE=47
    LT=48
    LTE=49
    STREQ=50
    STRADD=51
    DOUBLECOLON=52
    DOUBLEDOT=53
    ZERO=54
    INTLIT=55
    FLOATLIT=56
    STRINGLIT=57
    ID=58
    DOLLAR_ID=59
    COMMENT=60
    WS=61
    ERROR_CHAR=62
    UNCLOSE_STRING=63
    ILLEGAL_ESCAPE=64

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

        def classDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ClassDeclarationContext)
            else:
                return self.getTypedRuleContext(D96Parser.ClassDeclarationContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_program




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 98
                self.classDeclaration()
                self.state = 101 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==D96Parser.CLASS):
                    break

            self.state = 103
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(D96Parser.CLASS, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def classBody(self):
            return self.getTypedRuleContext(D96Parser.ClassBodyContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_classDeclaration




    def classDeclaration(self):

        localctx = D96Parser.ClassDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_classDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(D96Parser.CLASS)
            self.state = 106
            self.match(D96Parser.ID)
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COLON:
                self.state = 107
                self.match(D96Parser.COLON)
                self.state = 108
                self.match(D96Parser.ID)


            self.state = 111
            self.match(D96Parser.LP)
            self.state = 112
            self.classBody()
            self.state = 113
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassBodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attrDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.AttrDeclarationContext)
            else:
                return self.getTypedRuleContext(D96Parser.AttrDeclarationContext,i)


        def methodDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.MethodDeclarationContext)
            else:
                return self.getTypedRuleContext(D96Parser.MethodDeclarationContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_classBody




    def classBody(self):

        localctx = D96Parser.ClassBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_classBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.CONSTRUCTOR) | (1 << D96Parser.DESTRUCTOR) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLAR_ID))) != 0):
                self.state = 117
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.VAL, D96Parser.VAR]:
                    self.state = 115
                    self.attrDeclaration()
                    pass
                elif token in [D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.ID, D96Parser.DOLLAR_ID]:
                    self.state = 116
                    self.methodDeclaration()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 121
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttrDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.attr_counter = 1
            self.exp_counter = 1

        def attrList(self):
            return self.getTypedRuleContext(D96Parser.AttrListContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def typeName(self):
            return self.getTypedRuleContext(D96Parser.TypeNameContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_attrDeclaration




    def attrDeclaration(self):

        localctx = D96Parser.AttrDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_attrDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 123
            self.attrList()
            self.state = 124
            self.match(D96Parser.COLON)
            self.state = 125
            self.typeName()
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ASSIGN:
                self.state = 126
                self.match(D96Parser.ASSIGN)

                self.state = 127
                self.exp(0)
                self.state = 136
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 128
                        if not localctx.exp_counter <= localctx.attr_counter:
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "$exp_counter <= $attr_counter")

                        self.state = 129
                        self.match(D96Parser.COMMA)
                        self.state = 130
                        self.exp(0)
                        localctx.exp_counter = localctx.exp_counter + 1 
                    self.state = 138
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,4,self._ctx)



            self.state = 141
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttrListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.IdentifierContext)
            else:
                return self.getTypedRuleContext(D96Parser.IdentifierContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_attrList




    def attrList(self):

        localctx = D96Parser.AttrListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_attrList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.identifier()
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 144
                self.match(D96Parser.COMMA)
                self.state = 145
                self.identifier()
                self.state = 150
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_identifier




    def identifier(self):

        localctx = D96Parser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            _la = self._input.LA(1)
            if not(_la==D96Parser.ID or _la==D96Parser.DOLLAR_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeNameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitiveType(self):
            return self.getTypedRuleContext(D96Parser.PrimitiveTypeContext,0)


        def arrayType(self):
            return self.getTypedRuleContext(D96Parser.ArrayTypeContext,0)


        def classType(self):
            return self.getTypedRuleContext(D96Parser.ClassTypeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_typeName




    def typeName(self):

        localctx = D96Parser.TypeNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_typeName)
        try:
            self.state = 156
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 153
                self.primitiveType()
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 154
                self.arrayType()
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 155
                self.classType()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blockStmt(self):
            return self.getTypedRuleContext(D96Parser.BlockStmtContext,0)


        def identifier(self):
            return self.getTypedRuleContext(D96Parser.IdentifierContext,0)


        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def CONSTRUCTOR(self):
            return self.getToken(D96Parser.CONSTRUCTOR, 0)

        def DESTRUCTOR(self):
            return self.getToken(D96Parser.DESTRUCTOR, 0)

        def paraList(self):
            return self.getTypedRuleContext(D96Parser.ParaListContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_methodDeclaration




    def methodDeclaration(self):

        localctx = D96Parser.MethodDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_methodDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID, D96Parser.DOLLAR_ID]:
                self.state = 158
                self.identifier()
                self.state = 159
                self.match(D96Parser.LB)
                self.state = 161
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.ID:
                    self.state = 160
                    self.paraList()


                self.state = 163
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.CONSTRUCTOR]:
                self.state = 165
                self.match(D96Parser.CONSTRUCTOR)
                self.state = 166
                self.match(D96Parser.LB)
                self.state = 168
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.ID:
                    self.state = 167
                    self.paraList()


                self.state = 170
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.DESTRUCTOR]:
                self.state = 171
                self.match(D96Parser.DESTRUCTOR)
                self.state = 172
                self.match(D96Parser.LB)
                self.state = 173
                self.match(D96Parser.RB)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 176
            self.blockStmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParaListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paraDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ParaDeclarationContext)
            else:
                return self.getTypedRuleContext(D96Parser.ParaDeclarationContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.SEMI)
            else:
                return self.getToken(D96Parser.SEMI, i)

        def getRuleIndex(self):
            return D96Parser.RULE_paraList




    def paraList(self):

        localctx = D96Parser.ParaListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_paraList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.paraDeclaration()
            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.SEMI:
                self.state = 179
                self.match(D96Parser.SEMI)
                self.state = 180
                self.paraDeclaration()
                self.state = 185
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParaDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idList(self):
            return self.getTypedRuleContext(D96Parser.IdListContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def typeName(self):
            return self.getTypedRuleContext(D96Parser.TypeNameContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_paraDeclaration




    def paraDeclaration(self):

        localctx = D96Parser.ParaDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_paraDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.idList()
            self.state = 187
            self.match(D96Parser.COLON)
            self.state = 188
            self.typeName()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_idList




    def idList(self):

        localctx = D96Parser.IdListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_idList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.match(D96Parser.ID)
            self.state = 195
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 191
                self.match(D96Parser.COMMA)
                self.state = 192
                self.match(D96Parser.ID)
                self.state = 197
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimitiveTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLEAN(self):
            return self.getToken(D96Parser.BOOLEAN, 0)

        def INT(self):
            return self.getToken(D96Parser.INT, 0)

        def FLOAT(self):
            return self.getToken(D96Parser.FLOAT, 0)

        def STRING(self):
            return self.getToken(D96Parser.STRING, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_primitiveType




    def primitiveType(self):

        localctx = D96Parser.PrimitiveTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_primitiveType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.INT) | (1 << D96Parser.FLOAT) | (1 << D96Parser.BOOLEAN) | (1 << D96Parser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LS(self):
            return self.getToken(D96Parser.LS, 0)

        def elementType(self):
            return self.getTypedRuleContext(D96Parser.ElementTypeContext,0)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def INTLIT(self):
            return self.getToken(D96Parser.INTLIT, 0)

        def RS(self):
            return self.getToken(D96Parser.RS, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_arrayType




    def arrayType(self):

        localctx = D96Parser.ArrayTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_arrayType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.match(D96Parser.ARRAY)
            self.state = 201
            self.match(D96Parser.LS)
            self.state = 202
            self.elementType()
            self.state = 203
            self.match(D96Parser.COMMA)
            self.state = 204
            self.match(D96Parser.INTLIT)
            self.state = 205
            self.match(D96Parser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitiveType(self):
            return self.getTypedRuleContext(D96Parser.PrimitiveTypeContext,0)


        def arrayType(self):
            return self.getTypedRuleContext(D96Parser.ArrayTypeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_elementType




    def elementType(self):

        localctx = D96Parser.ElementTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_elementType)
        try:
            self.state = 209
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 207
                self.primitiveType()
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 208
                self.arrayType()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_classType




    def classType(self):

        localctx = D96Parser.ClassTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_classType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.match(D96Parser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignStmt(self):
            return self.getTypedRuleContext(D96Parser.AssignStmtContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(D96Parser.IfStmtContext,0)


        def forInStmt(self):
            return self.getTypedRuleContext(D96Parser.ForInStmtContext,0)


        def breakStmt(self):
            return self.getTypedRuleContext(D96Parser.BreakStmtContext,0)


        def continueStmt(self):
            return self.getTypedRuleContext(D96Parser.ContinueStmtContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(D96Parser.ReturnStmtContext,0)


        def instanceCall(self):
            return self.getTypedRuleContext(D96Parser.InstanceCallContext,0)


        def staticCall(self):
            return self.getTypedRuleContext(D96Parser.StaticCallContext,0)


        def blockStmt(self):
            return self.getTypedRuleContext(D96Parser.BlockStmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_stmt




    def stmt(self):

        localctx = D96Parser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_stmt)
        try:
            self.state = 222
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 213
                self.assignStmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 214
                self.ifStmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 215
                self.forInStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 216
                self.breakStmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 217
                self.continueStmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 218
                self.returnStmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 219
                self.instanceCall()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 220
                self.staticCall()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 221
                self.blockStmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.var_counter = 1
            self.exp_counter = 1

        def varList(self):
            return self.getTypedRuleContext(D96Parser.VarListContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def typeName(self):
            return self.getTypedRuleContext(D96Parser.TypeNameContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_declarationStmt




    def declarationStmt(self):

        localctx = D96Parser.DeclarationStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_declarationStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 225
            self.varList()
            self.state = 226
            self.match(D96Parser.COLON)
            self.state = 227
            self.typeName()
            self.state = 240
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ASSIGN:
                self.state = 228
                self.match(D96Parser.ASSIGN)

                self.state = 229
                self.exp(0)
                self.state = 237
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 230
                        if not localctx.exp_counter != localctx.var_counter:
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "$exp_counter != $var_counter")

                        self.state = 231
                        self.match(D96Parser.COMMA)
                        self.state = 232
                        self.exp(0)
                        localctx.exp_counter = localctx.exp_counter + 1 
                    self.state = 239
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,15,self._ctx)



            self.state = 242
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_varList




    def varList(self):

        localctx = D96Parser.VarListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_varList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.match(D96Parser.ID)
            self.state = 249
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 245
                self.match(D96Parser.COMMA)
                self.state = 246
                self.match(D96Parser.ID)
                self.state = 251
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignLHS(self):
            return self.getTypedRuleContext(D96Parser.AssignLHSContext,0)


        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_assignStmt




    def assignStmt(self):

        localctx = D96Parser.AssignStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_assignStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.assignLHS()
            self.state = 253
            self.match(D96Parser.ASSIGN)
            self.state = 254
            self.exp(0)
            self.state = 255
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignLHSContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def indexOperation(self):
            return self.getTypedRuleContext(D96Parser.IndexOperationContext,0)


        def scalar(self):
            return self.getTypedRuleContext(D96Parser.ScalarContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_assignLHS




    def assignLHS(self):

        localctx = D96Parser.AssignLHSContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_assignLHS)
        try:
            self.state = 259
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 257
                self.indexOperation()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 258
                self.scalar()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScalarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOUBLECOLON(self):
            return self.getToken(D96Parser.DOUBLECOLON, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_scalar




    def scalar(self):

        localctx = D96Parser.ScalarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_scalar)
        try:
            self.state = 269
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 261
                self.exp(0)
                self.state = 262
                self.match(D96Parser.DOT)
                self.state = 263
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 265
                self.match(D96Parser.ID)
                self.state = 266
                self.match(D96Parser.DOUBLECOLON)
                self.state = 267
                self.match(D96Parser.DOLLAR_ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 268
                self.match(D96Parser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexOperationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LS(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.LS)
            else:
                return self.getToken(D96Parser.LS, i)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpContext,i)


        def RS(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.RS)
            else:
                return self.getToken(D96Parser.RS, i)

        def getRuleIndex(self):
            return D96Parser.RULE_indexOperation




    def indexOperation(self):

        localctx = D96Parser.IndexOperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_indexOperation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.match(D96Parser.ID)
            self.state = 276 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 272
                self.match(D96Parser.LS)
                self.state = 273
                self.exp(0)
                self.state = 274
                self.match(D96Parser.RS)
                self.state = 278 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==D96Parser.LS):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(D96Parser.IF, 0)

        def ifBody(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.IfBodyContext)
            else:
                return self.getTypedRuleContext(D96Parser.IfBodyContext,i)


        def ELSEIF(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ELSEIF)
            else:
                return self.getToken(D96Parser.ELSEIF, i)

        def ELSE(self):
            return self.getToken(D96Parser.ELSE, 0)

        def blockStmt(self):
            return self.getTypedRuleContext(D96Parser.BlockStmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_ifStmt




    def ifStmt(self):

        localctx = D96Parser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_ifStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.match(D96Parser.IF)
            self.state = 281
            self.ifBody()
            self.state = 286
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.ELSEIF:
                self.state = 282
                self.match(D96Parser.ELSEIF)
                self.state = 283
                self.ifBody()
                self.state = 288
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 291
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ELSE:
                self.state = 289
                self.match(D96Parser.ELSE)
                self.state = 290
                self.blockStmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfBodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def blockStmt(self):
            return self.getTypedRuleContext(D96Parser.BlockStmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_ifBody




    def ifBody(self):

        localctx = D96Parser.IfBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_ifBody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.match(D96Parser.LB)
            self.state = 294
            self.exp(0)
            self.state = 295
            self.match(D96Parser.RB)
            self.state = 296
            self.blockStmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForInStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOREACH(self):
            return self.getToken(D96Parser.FOREACH, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def scalar(self):
            return self.getTypedRuleContext(D96Parser.ScalarContext,0)


        def IN(self):
            return self.getToken(D96Parser.IN, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpContext,i)


        def DOUBLEDOT(self):
            return self.getToken(D96Parser.DOUBLEDOT, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def blockStmt(self):
            return self.getTypedRuleContext(D96Parser.BlockStmtContext,0)


        def BY(self):
            return self.getToken(D96Parser.BY, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_forInStmt




    def forInStmt(self):

        localctx = D96Parser.ForInStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_forInStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.match(D96Parser.FOREACH)
            self.state = 299
            self.match(D96Parser.LB)
            self.state = 300
            self.scalar()
            self.state = 301
            self.match(D96Parser.IN)
            self.state = 302
            self.exp(0)
            self.state = 303
            self.match(D96Parser.DOUBLEDOT)
            self.state = 304
            self.exp(0)
            self.state = 307
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.BY:
                self.state = 305
                self.match(D96Parser.BY)
                self.state = 306
                self.exp(0)


            self.state = 309
            self.match(D96Parser.RB)
            self.state = 310
            self.blockStmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(D96Parser.BREAK, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_breakStmt




    def breakStmt(self):

        localctx = D96Parser.BreakStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_breakStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self.match(D96Parser.BREAK)
            self.state = 313
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(D96Parser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_continueStmt




    def continueStmt(self):

        localctx = D96Parser.ContinueStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_continueStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.match(D96Parser.CONTINUE)
            self.state = 316
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(D96Parser.RETURN, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_returnStmt




    def returnStmt(self):

        localctx = D96Parser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_returnStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.match(D96Parser.RETURN)
            self.state = 320
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.LB) | (1 << D96Parser.MINUS) | (1 << D96Parser.NOT) | (1 << D96Parser.ZERO) | (1 << D96Parser.INTLIT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.STRINGLIT) | (1 << D96Parser.ID))) != 0):
                self.state = 319
                self.exp(0)


            self.state = 322
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstanceCallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def expList(self):
            return self.getTypedRuleContext(D96Parser.ExpListContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_instanceCall




    def instanceCall(self):

        localctx = D96Parser.InstanceCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_instanceCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.exp(0)
            self.state = 325
            self.match(D96Parser.DOT)
            self.state = 326
            self.match(D96Parser.ID)
            self.state = 327
            self.match(D96Parser.LB)
            self.state = 329
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.LB) | (1 << D96Parser.MINUS) | (1 << D96Parser.NOT) | (1 << D96Parser.ZERO) | (1 << D96Parser.INTLIT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.STRINGLIT) | (1 << D96Parser.ID))) != 0):
                self.state = 328
                self.expList()


            self.state = 331
            self.match(D96Parser.RB)
            self.state = 332
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StaticCallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOUBLECOLON(self):
            return self.getToken(D96Parser.DOUBLECOLON, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def expList(self):
            return self.getTypedRuleContext(D96Parser.ExpListContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_staticCall




    def staticCall(self):

        localctx = D96Parser.StaticCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_staticCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.match(D96Parser.ID)
            self.state = 335
            self.match(D96Parser.DOUBLECOLON)
            self.state = 336
            self.match(D96Parser.DOLLAR_ID)
            self.state = 337
            self.match(D96Parser.LB)
            self.state = 339
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.LB) | (1 << D96Parser.MINUS) | (1 << D96Parser.NOT) | (1 << D96Parser.ZERO) | (1 << D96Parser.INTLIT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.STRINGLIT) | (1 << D96Parser.ID))) != 0):
                self.state = 338
                self.expList()


            self.state = 341
            self.match(D96Parser.RB)
            self.state = 342
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def declarationStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.DeclarationStmtContext)
            else:
                return self.getTypedRuleContext(D96Parser.DeclarationStmtContext,i)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.StmtContext)
            else:
                return self.getTypedRuleContext(D96Parser.StmtContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_blockStmt




    def blockStmt(self):

        localctx = D96Parser.BlockStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_blockStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 344
            self.match(D96Parser.LP)
            self.state = 349
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.BREAK) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.IF) | (1 << D96Parser.FOREACH) | (1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.ARRAY) | (1 << D96Parser.RETURN) | (1 << D96Parser.NULL) | (1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.LB) | (1 << D96Parser.LP) | (1 << D96Parser.MINUS) | (1 << D96Parser.NOT) | (1 << D96Parser.ZERO) | (1 << D96Parser.INTLIT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.STRINGLIT) | (1 << D96Parser.ID))) != 0):
                self.state = 347
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.VAL, D96Parser.VAR]:
                    self.state = 345
                    self.declarationStmt()
                    pass
                elif token in [D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.IF, D96Parser.FOREACH, D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.RETURN, D96Parser.NULL, D96Parser.SELF, D96Parser.NEW, D96Parser.LB, D96Parser.LP, D96Parser.MINUS, D96Parser.NOT, D96Parser.ZERO, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.ID]:
                    self.state = 346
                    self.stmt()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 351
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 352
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self):
            return self.getTypedRuleContext(D96Parser.Exp1Context,0)


        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpContext,i)


        def STRADD(self):
            return self.getToken(D96Parser.STRADD, 0)

        def STREQ(self):
            return self.getToken(D96Parser.STREQ, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp



    def exp(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.ExpContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_exp, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
            self.exp1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 362
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.ExpContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                    self.state = 357
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 358
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.STREQ or _la==D96Parser.STRADD):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 359
                    self.exp(3) 
                self.state = 364
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self):
            return self.getTypedRuleContext(D96Parser.Exp2Context,0)


        def exp1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Exp1Context)
            else:
                return self.getTypedRuleContext(D96Parser.Exp1Context,i)


        def EQUAL(self):
            return self.getToken(D96Parser.EQUAL, 0)

        def DIFF(self):
            return self.getToken(D96Parser.DIFF, 0)

        def LT(self):
            return self.getToken(D96Parser.LT, 0)

        def LTE(self):
            return self.getToken(D96Parser.LTE, 0)

        def GT(self):
            return self.getToken(D96Parser.GT, 0)

        def GTE(self):
            return self.getToken(D96Parser.GTE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp1



    def exp1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_exp1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            self.exp2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 373
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                    self.state = 368
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 369
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.EQUAL) | (1 << D96Parser.DIFF) | (1 << D96Parser.GT) | (1 << D96Parser.GTE) | (1 << D96Parser.LT) | (1 << D96Parser.LTE))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 370
                    self.exp1(3) 
                self.state = 375
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(D96Parser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(D96Parser.Exp2Context,0)


        def AND(self):
            return self.getToken(D96Parser.AND, 0)

        def OR(self):
            return self.getToken(D96Parser.OR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp2



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_exp2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 384
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 379
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 380
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.AND or _la==D96Parser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 381
                    self.exp3(0) 
                self.state = 386
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(D96Parser.Exp4Context,0)


        def exp3(self):
            return self.getTypedRuleContext(D96Parser.Exp3Context,0)


        def ADD(self):
            return self.getToken(D96Parser.ADD, 0)

        def MINUS(self):
            return self.getToken(D96Parser.MINUS, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp3



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_exp3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 395
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 390
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 391
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ADD or _la==D96Parser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 392
                    self.exp4(0) 
                self.state = 397
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp5(self):
            return self.getTypedRuleContext(D96Parser.Exp5Context,0)


        def exp4(self):
            return self.getTypedRuleContext(D96Parser.Exp4Context,0)


        def MUL(self):
            return self.getToken(D96Parser.MUL, 0)

        def DIV(self):
            return self.getToken(D96Parser.DIV, 0)

        def MOD(self):
            return self.getToken(D96Parser.MOD, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp4



    def exp4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_exp4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
            self.exp5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 406
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                    self.state = 401
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 402
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.MUL) | (1 << D96Parser.DIV) | (1 << D96Parser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 403
                    self.exp5() 
                self.state = 408
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp5Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(D96Parser.NOT, 0)

        def exp5(self):
            return self.getTypedRuleContext(D96Parser.Exp5Context,0)


        def exp6(self):
            return self.getTypedRuleContext(D96Parser.Exp6Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp5




    def exp5(self):

        localctx = D96Parser.Exp5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_exp5)
        try:
            self.state = 412
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 409
                self.match(D96Parser.NOT)
                self.state = 410
                self.exp5()
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.SELF, D96Parser.NEW, D96Parser.LB, D96Parser.MINUS, D96Parser.ZERO, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 411
                self.exp6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp6Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(D96Parser.MINUS, 0)

        def exp6(self):
            return self.getTypedRuleContext(D96Parser.Exp6Context,0)


        def exp7(self):
            return self.getTypedRuleContext(D96Parser.Exp7Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp6




    def exp6(self):

        localctx = D96Parser.Exp6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_exp6)
        try:
            self.state = 417
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 414
                self.match(D96Parser.MINUS)
                self.state = 415
                self.exp6()
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.SELF, D96Parser.NEW, D96Parser.LB, D96Parser.ZERO, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 416
                self.exp7(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp7Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp8(self):
            return self.getTypedRuleContext(D96Parser.Exp8Context,0)


        def exp7(self):
            return self.getTypedRuleContext(D96Parser.Exp7Context,0)


        def LS(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.LS)
            else:
                return self.getToken(D96Parser.LS, i)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpContext,i)


        def RS(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.RS)
            else:
                return self.getToken(D96Parser.RS, i)

        def getRuleIndex(self):
            return D96Parser.RULE_exp7



    def exp7(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp7Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_exp7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            self.exp8(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 433
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp7)
                    self.state = 422
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 427 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 423
                            self.match(D96Parser.LS)
                            self.state = 424
                            self.exp(0)
                            self.state = 425
                            self.match(D96Parser.RS)

                        else:
                            raise NoViableAltException(self)
                        self.state = 429 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
             
                self.state = 435
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp8Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp9(self):
            return self.getTypedRuleContext(D96Parser.Exp9Context,0)


        def exp8(self):
            return self.getTypedRuleContext(D96Parser.Exp8Context,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def expList(self):
            return self.getTypedRuleContext(D96Parser.ExpListContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp8



    def exp8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_exp8, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 437
            self.exp9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 451
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp8)
                    self.state = 439
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 440
                    self.match(D96Parser.DOT)
                    self.state = 441
                    self.match(D96Parser.ID)
                    self.state = 447
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
                    if la_ == 1:
                        self.state = 442
                        self.match(D96Parser.LB)
                        self.state = 444
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.LB) | (1 << D96Parser.MINUS) | (1 << D96Parser.NOT) | (1 << D96Parser.ZERO) | (1 << D96Parser.INTLIT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.STRINGLIT) | (1 << D96Parser.ID))) != 0):
                            self.state = 443
                            self.expList()


                        self.state = 446
                        self.match(D96Parser.RB)

             
                self.state = 453
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp9Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOUBLECOLON(self):
            return self.getToken(D96Parser.DOUBLECOLON, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def expList(self):
            return self.getTypedRuleContext(D96Parser.ExpListContext,0)


        def exp10(self):
            return self.getTypedRuleContext(D96Parser.Exp10Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp9




    def exp9(self):

        localctx = D96Parser.Exp9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_exp9)
        self._la = 0 # Token type
        try:
            self.state = 465
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 454
                self.match(D96Parser.ID)
                self.state = 455
                self.match(D96Parser.DOUBLECOLON)
                self.state = 456
                self.match(D96Parser.DOLLAR_ID)
                self.state = 462
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
                if la_ == 1:
                    self.state = 457
                    self.match(D96Parser.LB)
                    self.state = 459
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.LB) | (1 << D96Parser.MINUS) | (1 << D96Parser.NOT) | (1 << D96Parser.ZERO) | (1 << D96Parser.INTLIT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.STRINGLIT) | (1 << D96Parser.ID))) != 0):
                        self.state = 458
                        self.expList()


                    self.state = 461
                    self.match(D96Parser.RB)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 464
                self.exp10()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp10Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(D96Parser.NEW, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def expList(self):
            return self.getTypedRuleContext(D96Parser.ExpListContext,0)


        def exp11(self):
            return self.getTypedRuleContext(D96Parser.Exp11Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp10




    def exp10(self):

        localctx = D96Parser.Exp10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_exp10)
        self._la = 0 # Token type
        try:
            self.state = 475
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 467
                self.match(D96Parser.NEW)
                self.state = 468
                self.match(D96Parser.ID)
                self.state = 469
                self.match(D96Parser.LB)
                self.state = 471
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.LB) | (1 << D96Parser.MINUS) | (1 << D96Parser.NOT) | (1 << D96Parser.ZERO) | (1 << D96Parser.INTLIT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.STRINGLIT) | (1 << D96Parser.ID))) != 0):
                    self.state = 470
                    self.expList()


                self.state = 473
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.SELF, D96Parser.LB, D96Parser.ZERO, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 474
                self.exp11()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp11Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def operand(self):
            return self.getTypedRuleContext(D96Parser.OperandContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp11




    def exp11(self):

        localctx = D96Parser.Exp11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_exp11)
        try:
            self.state = 482
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 477
                self.match(D96Parser.LB)
                self.state = 478
                self.exp(0)
                self.state = 479
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.SELF, D96Parser.ZERO, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 481
                self.operand()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_expList




    def expList(self):

        localctx = D96Parser.ExpListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_expList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 484
            self.exp(0)
            self.state = 489
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 485
                self.match(D96Parser.COMMA)
                self.state = 486
                self.exp(0)
                self.state = 491
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def ZERO(self):
            return self.getToken(D96Parser.ZERO, 0)

        def INTLIT(self):
            return self.getToken(D96Parser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(D96Parser.FLOATLIT, 0)

        def STRINGLIT(self):
            return self.getToken(D96Parser.STRINGLIT, 0)

        def booleanLit(self):
            return self.getTypedRuleContext(D96Parser.BooleanLitContext,0)


        def indexArray(self):
            return self.getTypedRuleContext(D96Parser.IndexArrayContext,0)


        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def NULL(self):
            return self.getToken(D96Parser.NULL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_operand




    def operand(self):

        localctx = D96Parser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_operand)
        try:
            self.state = 501
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 492
                self.match(D96Parser.ID)
                pass
            elif token in [D96Parser.ZERO]:
                self.enterOuterAlt(localctx, 2)
                self.state = 493
                self.match(D96Parser.ZERO)
                pass
            elif token in [D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 494
                self.match(D96Parser.INTLIT)
                pass
            elif token in [D96Parser.FLOATLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 495
                self.match(D96Parser.FLOATLIT)
                pass
            elif token in [D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 496
                self.match(D96Parser.STRINGLIT)
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE]:
                self.enterOuterAlt(localctx, 6)
                self.state = 497
                self.booleanLit()
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 7)
                self.state = 498
                self.indexArray()
                pass
            elif token in [D96Parser.SELF]:
                self.enterOuterAlt(localctx, 8)
                self.state = 499
                self.match(D96Parser.SELF)
                pass
            elif token in [D96Parser.NULL]:
                self.enterOuterAlt(localctx, 9)
                self.state = 500
                self.match(D96Parser.NULL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexArrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def arrayBody(self):
            return self.getTypedRuleContext(D96Parser.ArrayBodyContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_indexArray




    def indexArray(self):

        localctx = D96Parser.IndexArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_indexArray)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 503
            self.match(D96Parser.ARRAY)
            self.state = 504
            self.match(D96Parser.LB)
            self.state = 506
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.LB) | (1 << D96Parser.MINUS) | (1 << D96Parser.NOT) | (1 << D96Parser.ZERO) | (1 << D96Parser.INTLIT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.STRINGLIT) | (1 << D96Parser.ID))) != 0):
                self.state = 505
                self.arrayBody()


            self.state = 508
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayBodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrayLit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ArrayLitContext)
            else:
                return self.getTypedRuleContext(D96Parser.ArrayLitContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_arrayBody




    def arrayBody(self):

        localctx = D96Parser.ArrayBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_arrayBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 510
            self.arrayLit()
            self.state = 515
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 511
                self.match(D96Parser.COMMA)
                self.state = 512
                self.arrayLit()
                self.state = 517
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayLitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def indexArray(self):
            return self.getTypedRuleContext(D96Parser.IndexArrayContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_arrayLit




    def arrayLit(self):

        localctx = D96Parser.ArrayLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_arrayLit)
        try:
            self.state = 520
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 518
                self.exp(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 519
                self.indexArray()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanLitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(D96Parser.TRUE, 0)

        def FALSE(self):
            return self.getToken(D96Parser.FALSE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_booleanLit




    def booleanLit(self):

        localctx = D96Parser.BooleanLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_booleanLit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 522
            _la = self._input.LA(1)
            if not(_la==D96Parser.TRUE or _la==D96Parser.FALSE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.attrDeclaration_sempred
        self._predicates[16] = self.declarationStmt_sempred
        self._predicates[31] = self.exp_sempred
        self._predicates[32] = self.exp1_sempred
        self._predicates[33] = self.exp2_sempred
        self._predicates[34] = self.exp3_sempred
        self._predicates[35] = self.exp4_sempred
        self._predicates[38] = self.exp7_sempred
        self._predicates[39] = self.exp8_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def attrDeclaration_sempred(self, localctx:AttrDeclarationContext, predIndex:int):
            if predIndex == 0:
                return localctx.exp_counter <= localctx.attr_counter
         

    def declarationStmt_sempred(self, localctx:DeclarationStmtContext, predIndex:int):
            if predIndex == 1:
                return localctx.exp_counter != localctx.var_counter
         

    def exp_sempred(self, localctx:ExpContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def exp1_sempred(self, localctx:Exp1Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

    def exp4_sempred(self, localctx:Exp4Context, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         

    def exp7_sempred(self, localctx:Exp7Context, predIndex:int):
            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         

    def exp8_sempred(self, localctx:Exp8Context, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 2)
         




