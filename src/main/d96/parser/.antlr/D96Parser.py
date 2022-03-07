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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3E")
        buf.write("\u0229\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\3\2\6")
        buf.write("\2v\n\2\r\2\16\2w\3\2\3\2\3\3\3\3\3\3\3\3\5\3\u0080\n")
        buf.write("\3\3\3\3\3\3\3\3\3\3\4\3\4\7\4\u0088\n\4\f\4\16\4\u008b")
        buf.write("\13\4\3\5\3\5\3\5\5\5\u0090\n\5\3\5\3\5\3\6\3\6\3\6\3")
        buf.write("\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u00a2\n")
        buf.write("\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\7\t\u00ab\n\t\f\t\16\t")
        buf.write("\u00ae\13\t\3\n\3\n\3\13\3\13\3\13\5\13\u00b5\n\13\3\f")
        buf.write("\3\f\3\f\5\f\u00ba\n\f\3\f\3\f\3\f\3\f\3\f\5\f\u00c1\n")
        buf.write("\f\3\f\3\f\3\f\3\f\5\f\u00c7\n\f\3\f\3\f\3\r\3\r\3\r\7")
        buf.write("\r\u00ce\n\r\f\r\16\r\u00d1\13\r\3\16\3\16\3\16\3\16\3")
        buf.write("\17\3\17\3\17\7\17\u00da\n\17\f\17\16\17\u00dd\13\17\3")
        buf.write("\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\5\22\u00ea\n\22\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3")
        buf.write("\24\3\24\3\24\3\24\3\24\5\24\u00f8\n\24\3\25\3\25\3\25")
        buf.write("\5\25\u00fd\n\25\3\25\3\25\3\26\3\26\3\26\3\26\3\27\3")
        buf.write("\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\5\27\u010f")
        buf.write("\n\27\3\30\3\30\3\30\3\30\3\31\3\31\3\31\7\31\u0118\n")
        buf.write("\31\f\31\16\31\u011b\13\31\3\32\3\32\3\32\3\32\3\32\3")
        buf.write("\33\3\33\5\33\u0124\n\33\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\5\34\u012e\n\34\3\35\3\35\3\36\3\36\3\37\3")
        buf.write("\37\3\37\3\37\7\37\u0138\n\37\f\37\16\37\u013b\13\37\3")
        buf.write("\37\3\37\5\37\u013f\n\37\3 \3 \3 \3 \3 \3!\3!\3!\3!\3")
        buf.write("!\3!\3!\3!\3!\5!\u014f\n!\3!\3!\3!\3\"\3\"\3\"\3#\3#\3")
        buf.write("#\3$\3$\5$\u015c\n$\3$\3$\3%\3%\3%\3%\3%\5%\u0165\n%\3")
        buf.write("%\3%\3%\3&\3&\3&\3&\3&\5&\u016f\n&\3&\3&\3&\3\'\3\'\7")
        buf.write("\'\u0176\n\'\f\'\16\'\u0179\13\'\3\'\3\'\3(\3(\3(\3(\3")
        buf.write("(\3(\7(\u0183\n(\f(\16(\u0186\13(\3)\3)\3)\3)\3)\3)\7")
        buf.write(")\u018e\n)\f)\16)\u0191\13)\3*\3*\3*\3*\3*\3*\7*\u0199")
        buf.write("\n*\f*\16*\u019c\13*\3+\3+\3+\3+\3+\3+\7+\u01a4\n+\f+")
        buf.write("\16+\u01a7\13+\3,\3,\3,\3,\3,\3,\7,\u01af\n,\f,\16,\u01b2")
        buf.write("\13,\3-\3-\3-\5-\u01b7\n-\3.\3.\3.\5.\u01bc\n.\3/\3/\3")
        buf.write("/\3/\3/\3/\3/\3/\6/\u01c6\n/\r/\16/\u01c7\7/\u01ca\n/")
        buf.write("\f/\16/\u01cd\13/\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3")
        buf.write("\60\5\60\u01d7\n\60\3\60\5\60\u01da\n\60\7\60\u01dc\n")
        buf.write("\60\f\60\16\60\u01df\13\60\3\61\3\61\3\61\3\61\3\61\5")
        buf.write("\61\u01e6\n\61\3\61\5\61\u01e9\n\61\3\61\5\61\u01ec\n")
        buf.write("\61\3\62\3\62\3\62\3\62\5\62\u01f2\n\62\3\62\3\62\5\62")
        buf.write("\u01f6\n\62\3\63\3\63\3\63\3\63\3\63\5\63\u01fd\n\63\3")
        buf.write("\64\3\64\3\64\7\64\u0202\n\64\f\64\16\64\u0205\13\64\3")
        buf.write("\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\5\65\u0210")
        buf.write("\n\65\3\66\3\66\3\66\5\66\u0215\n\66\3\66\3\66\3\67\3")
        buf.write("\67\3\67\7\67\u021c\n\67\f\67\16\67\u021f\13\67\38\38")
        buf.write("\58\u0223\n8\39\39\3:\3:\3:\2\tNPRTV\\^;\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDF")
        buf.write("HJLNPRTVXZ\\^`bdfhjlnpr\2\f\3\2\24\25\3\2?@\3\2\r\20\3")
        buf.write("\2\64\65\4\2--/\63\3\2+,\3\2%&\3\2\')\3\29<\3\2\t\n\2")
        buf.write("\u0233\2u\3\2\2\2\4{\3\2\2\2\6\u0089\3\2\2\2\b\u008c\3")
        buf.write("\2\2\2\n\u0093\3\2\2\2\f\u00a1\3\2\2\2\16\u00a3\3\2\2")
        buf.write("\2\20\u00a7\3\2\2\2\22\u00af\3\2\2\2\24\u00b4\3\2\2\2")
        buf.write("\26\u00c6\3\2\2\2\30\u00ca\3\2\2\2\32\u00d2\3\2\2\2\34")
        buf.write("\u00d6\3\2\2\2\36\u00de\3\2\2\2 \u00e0\3\2\2\2\"\u00e9")
        buf.write("\3\2\2\2$\u00eb\3\2\2\2&\u00f7\3\2\2\2(\u00f9\3\2\2\2")
        buf.write("*\u0100\3\2\2\2,\u010e\3\2\2\2.\u0110\3\2\2\2\60\u0114")
        buf.write("\3\2\2\2\62\u011c\3\2\2\2\64\u0123\3\2\2\2\66\u012d\3")
        buf.write("\2\2\28\u012f\3\2\2\2:\u0131\3\2\2\2<\u0133\3\2\2\2>\u0140")
        buf.write("\3\2\2\2@\u0145\3\2\2\2B\u0153\3\2\2\2D\u0156\3\2\2\2")
        buf.write("F\u0159\3\2\2\2H\u015f\3\2\2\2J\u0169\3\2\2\2L\u0173\3")
        buf.write("\2\2\2N\u017c\3\2\2\2P\u0187\3\2\2\2R\u0192\3\2\2\2T\u019d")
        buf.write("\3\2\2\2V\u01a8\3\2\2\2X\u01b6\3\2\2\2Z\u01bb\3\2\2\2")
        buf.write("\\\u01bd\3\2\2\2^\u01ce\3\2\2\2`\u01eb\3\2\2\2b\u01f5")
        buf.write("\3\2\2\2d\u01fc\3\2\2\2f\u01fe\3\2\2\2h\u020f\3\2\2\2")
        buf.write("j\u0211\3\2\2\2l\u0218\3\2\2\2n\u0222\3\2\2\2p\u0224\3")
        buf.write("\2\2\2r\u0226\3\2\2\2tv\5\4\3\2ut\3\2\2\2vw\3\2\2\2wu")
        buf.write("\3\2\2\2wx\3\2\2\2xy\3\2\2\2yz\7\2\2\3z\3\3\2\2\2{|\7")
        buf.write("\23\2\2|\177\7?\2\2}~\7$\2\2~\u0080\7?\2\2\177}\3\2\2")
        buf.write("\2\177\u0080\3\2\2\2\u0080\u0081\3\2\2\2\u0081\u0082\7")
        buf.write("\"\2\2\u0082\u0083\5\6\4\2\u0083\u0084\7#\2\2\u0084\5")
        buf.write("\3\2\2\2\u0085\u0088\5\b\5\2\u0086\u0088\5\26\f\2\u0087")
        buf.write("\u0085\3\2\2\2\u0087\u0086\3\2\2\2\u0088\u008b\3\2\2\2")
        buf.write("\u0089\u0087\3\2\2\2\u0089\u008a\3\2\2\2\u008a\7\3\2\2")
        buf.write("\2\u008b\u0089\3\2\2\2\u008c\u008f\t\2\2\2\u008d\u0090")
        buf.write("\5\n\6\2\u008e\u0090\5\16\b\2\u008f\u008d\3\2\2\2\u008f")
        buf.write("\u008e\3\2\2\2\u0090\u0091\3\2\2\2\u0091\u0092\7!\2\2")
        buf.write("\u0092\t\3\2\2\2\u0093\u0094\5\22\n\2\u0094\u0095\5\f")
        buf.write("\7\2\u0095\u0096\5N(\2\u0096\13\3\2\2\2\u0097\u0098\7")
        buf.write(" \2\2\u0098\u0099\5\22\n\2\u0099\u009a\5\f\7\2\u009a\u009b")
        buf.write("\5N(\2\u009b\u009c\7 \2\2\u009c\u00a2\3\2\2\2\u009d\u009e")
        buf.write("\7$\2\2\u009e\u009f\5\24\13\2\u009f\u00a0\7.\2\2\u00a0")
        buf.write("\u00a2\3\2\2\2\u00a1\u0097\3\2\2\2\u00a1\u009d\3\2\2\2")
        buf.write("\u00a2\r\3\2\2\2\u00a3\u00a4\5\20\t\2\u00a4\u00a5\7$\2")
        buf.write("\2\u00a5\u00a6\5\24\13\2\u00a6\17\3\2\2\2\u00a7\u00ac")
        buf.write("\5\22\n\2\u00a8\u00a9\7 \2\2\u00a9\u00ab\5\22\n\2\u00aa")
        buf.write("\u00a8\3\2\2\2\u00ab\u00ae\3\2\2\2\u00ac\u00aa\3\2\2\2")
        buf.write("\u00ac\u00ad\3\2\2\2\u00ad\21\3\2\2\2\u00ae\u00ac\3\2")
        buf.write("\2\2\u00af\u00b0\t\3\2\2\u00b0\23\3\2\2\2\u00b1\u00b5")
        buf.write("\5\36\20\2\u00b2\u00b5\5 \21\2\u00b3\u00b5\5$\23\2\u00b4")
        buf.write("\u00b1\3\2\2\2\u00b4\u00b2\3\2\2\2\u00b4\u00b3\3\2\2\2")
        buf.write("\u00b5\25\3\2\2\2\u00b6\u00b7\5\22\n\2\u00b7\u00b9\7\33")
        buf.write("\2\2\u00b8\u00ba\5\30\r\2\u00b9\u00b8\3\2\2\2\u00b9\u00ba")
        buf.write("\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\u00bc\7\34\2\2\u00bc")
        buf.write("\u00c7\3\2\2\2\u00bd\u00be\7\27\2\2\u00be\u00c0\7\33\2")
        buf.write("\2\u00bf\u00c1\5\30\r\2\u00c0\u00bf\3\2\2\2\u00c0\u00c1")
        buf.write("\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2\u00c7\7\34\2\2\u00c3")
        buf.write("\u00c4\7\30\2\2\u00c4\u00c5\7\33\2\2\u00c5\u00c7\7\34")
        buf.write("\2\2\u00c6\u00b6\3\2\2\2\u00c6\u00bd\3\2\2\2\u00c6\u00c3")
        buf.write("\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8\u00c9\5L\'\2\u00c9")
        buf.write("\27\3\2\2\2\u00ca\u00cf\5\32\16\2\u00cb\u00cc\7!\2\2\u00cc")
        buf.write("\u00ce\5\32\16\2\u00cd\u00cb\3\2\2\2\u00ce\u00d1\3\2\2")
        buf.write("\2\u00cf\u00cd\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0\31\3")
        buf.write("\2\2\2\u00d1\u00cf\3\2\2\2\u00d2\u00d3\5\34\17\2\u00d3")
        buf.write("\u00d4\7$\2\2\u00d4\u00d5\5\24\13\2\u00d5\33\3\2\2\2\u00d6")
        buf.write("\u00db\7?\2\2\u00d7\u00d8\7 \2\2\u00d8\u00da\7?\2\2\u00d9")
        buf.write("\u00d7\3\2\2\2\u00da\u00dd\3\2\2\2\u00db\u00d9\3\2\2\2")
        buf.write("\u00db\u00dc\3\2\2\2\u00dc\35\3\2\2\2\u00dd\u00db\3\2")
        buf.write("\2\2\u00de\u00df\t\4\2\2\u00df\37\3\2\2\2\u00e0\u00e1")
        buf.write("\7\13\2\2\u00e1\u00e2\7\35\2\2\u00e2\u00e3\5\"\22\2\u00e3")
        buf.write("\u00e4\7 \2\2\u00e4\u00e5\5p9\2\u00e5\u00e6\7\36\2\2\u00e6")
        buf.write("!\3\2\2\2\u00e7\u00ea\5\36\20\2\u00e8\u00ea\5 \21\2\u00e9")
        buf.write("\u00e7\3\2\2\2\u00e9\u00e8\3\2\2\2\u00ea#\3\2\2\2\u00eb")
        buf.write("\u00ec\7?\2\2\u00ec%\3\2\2\2\u00ed\u00f8\5\62\32\2\u00ee")
        buf.write("\u00f8\5<\37\2\u00ef\u00f8\5@!\2\u00f0\u00f8\5B\"\2\u00f1")
        buf.write("\u00f8\5D#\2\u00f2\u00f8\5F$\2\u00f3\u00f8\5H%\2\u00f4")
        buf.write("\u00f8\5J&\2\u00f5\u00f8\5(\25\2\u00f6\u00f8\5L\'\2\u00f7")
        buf.write("\u00ed\3\2\2\2\u00f7\u00ee\3\2\2\2\u00f7\u00ef\3\2\2\2")
        buf.write("\u00f7\u00f0\3\2\2\2\u00f7\u00f1\3\2\2\2\u00f7\u00f2\3")
        buf.write("\2\2\2\u00f7\u00f3\3\2\2\2\u00f7\u00f4\3\2\2\2\u00f7\u00f5")
        buf.write("\3\2\2\2\u00f7\u00f6\3\2\2\2\u00f8\'\3\2\2\2\u00f9\u00fc")
        buf.write("\t\2\2\2\u00fa\u00fd\5*\26\2\u00fb\u00fd\5.\30\2\u00fc")
        buf.write("\u00fa\3\2\2\2\u00fc\u00fb\3\2\2\2\u00fd\u00fe\3\2\2\2")
        buf.write("\u00fe\u00ff\7!\2\2\u00ff)\3\2\2\2\u0100\u0101\7?\2\2")
        buf.write("\u0101\u0102\5,\27\2\u0102\u0103\5N(\2\u0103+\3\2\2\2")
        buf.write("\u0104\u0105\7 \2\2\u0105\u0106\7?\2\2\u0106\u0107\5,")
        buf.write("\27\2\u0107\u0108\5N(\2\u0108\u0109\7 \2\2\u0109\u010f")
        buf.write("\3\2\2\2\u010a\u010b\7$\2\2\u010b\u010c\5\24\13\2\u010c")
        buf.write("\u010d\7.\2\2\u010d\u010f\3\2\2\2\u010e\u0104\3\2\2\2")
        buf.write("\u010e\u010a\3\2\2\2\u010f-\3\2\2\2\u0110\u0111\5\60\31")
        buf.write("\2\u0111\u0112\7$\2\2\u0112\u0113\5\24\13\2\u0113/\3\2")
        buf.write("\2\2\u0114\u0119\7?\2\2\u0115\u0116\7 \2\2\u0116\u0118")
        buf.write("\7?\2\2\u0117\u0115\3\2\2\2\u0118\u011b\3\2\2\2\u0119")
        buf.write("\u0117\3\2\2\2\u0119\u011a\3\2\2\2\u011a\61\3\2\2\2\u011b")
        buf.write("\u0119\3\2\2\2\u011c\u011d\5\64\33\2\u011d\u011e\7.\2")
        buf.write("\2\u011e\u011f\5N(\2\u011f\u0120\7!\2\2\u0120\63\3\2\2")
        buf.write("\2\u0121\u0124\58\35\2\u0122\u0124\5\66\34\2\u0123\u0121")
        buf.write("\3\2\2\2\u0123\u0122\3\2\2\2\u0124\65\3\2\2\2\u0125\u0126")
        buf.write("\5N(\2\u0126\u0127\7\37\2\2\u0127\u0128\7?\2\2\u0128\u012e")
        buf.write("\3\2\2\2\u0129\u012a\7?\2\2\u012a\u012b\7\66\2\2\u012b")
        buf.write("\u012e\7@\2\2\u012c\u012e\7?\2\2\u012d\u0125\3\2\2\2\u012d")
        buf.write("\u0129\3\2\2\2\u012d\u012c\3\2\2\2\u012e\67\3\2\2\2\u012f")
        buf.write("\u0130\5\\/\2\u01309\3\2\2\2\u0131\u0132\5N(\2\u0132;")
        buf.write("\3\2\2\2\u0133\u0134\7\5\2\2\u0134\u0139\5> \2\u0135\u0136")
        buf.write("\7\6\2\2\u0136\u0138\5> \2\u0137\u0135\3\2\2\2\u0138\u013b")
        buf.write("\3\2\2\2\u0139\u0137\3\2\2\2\u0139\u013a\3\2\2\2\u013a")
        buf.write("\u013e\3\2\2\2\u013b\u0139\3\2\2\2\u013c\u013d\7\7\2\2")
        buf.write("\u013d\u013f\5L\'\2\u013e\u013c\3\2\2\2\u013e\u013f\3")
        buf.write("\2\2\2\u013f=\3\2\2\2\u0140\u0141\7\33\2\2\u0141\u0142")
        buf.write("\5N(\2\u0142\u0143\7\34\2\2\u0143\u0144\5L\'\2\u0144?")
        buf.write("\3\2\2\2\u0145\u0146\7\b\2\2\u0146\u0147\7\33\2\2\u0147")
        buf.write("\u0148\5\66\34\2\u0148\u0149\7\f\2\2\u0149\u014a\5N(\2")
        buf.write("\u014a\u014b\7\67\2\2\u014b\u014e\5N(\2\u014c\u014d\7")
        buf.write("\32\2\2\u014d\u014f\5N(\2\u014e\u014c\3\2\2\2\u014e\u014f")
        buf.write("\3\2\2\2\u014f\u0150\3\2\2\2\u0150\u0151\7\34\2\2\u0151")
        buf.write("\u0152\5L\'\2\u0152A\3\2\2\2\u0153\u0154\7\3\2\2\u0154")
        buf.write("\u0155\7!\2\2\u0155C\3\2\2\2\u0156\u0157\7\4\2\2\u0157")
        buf.write("\u0158\7!\2\2\u0158E\3\2\2\2\u0159\u015b\7\21\2\2\u015a")
        buf.write("\u015c\5N(\2\u015b\u015a\3\2\2\2\u015b\u015c\3\2\2\2\u015c")
        buf.write("\u015d\3\2\2\2\u015d\u015e\7!\2\2\u015eG\3\2\2\2\u015f")
        buf.write("\u0160\5N(\2\u0160\u0161\7\37\2\2\u0161\u0162\7?\2\2\u0162")
        buf.write("\u0164\7\33\2\2\u0163\u0165\5f\64\2\u0164\u0163\3\2\2")
        buf.write("\2\u0164\u0165\3\2\2\2\u0165\u0166\3\2\2\2\u0166\u0167")
        buf.write("\7\34\2\2\u0167\u0168\7!\2\2\u0168I\3\2\2\2\u0169\u016a")
        buf.write("\7?\2\2\u016a\u016b\7\66\2\2\u016b\u016c\7@\2\2\u016c")
        buf.write("\u016e\7\33\2\2\u016d\u016f\5f\64\2\u016e\u016d\3\2\2")
        buf.write("\2\u016e\u016f\3\2\2\2\u016f\u0170\3\2\2\2\u0170\u0171")
        buf.write("\7\34\2\2\u0171\u0172\7!\2\2\u0172K\3\2\2\2\u0173\u0177")
        buf.write("\7\"\2\2\u0174\u0176\5&\24\2\u0175\u0174\3\2\2\2\u0176")
        buf.write("\u0179\3\2\2\2\u0177\u0175\3\2\2\2\u0177\u0178\3\2\2\2")
        buf.write("\u0178\u017a\3\2\2\2\u0179\u0177\3\2\2\2\u017a\u017b\7")
        buf.write("#\2\2\u017bM\3\2\2\2\u017c\u017d\b(\1\2\u017d\u017e\5")
        buf.write("P)\2\u017e\u0184\3\2\2\2\u017f\u0180\f\4\2\2\u0180\u0181")
        buf.write("\t\5\2\2\u0181\u0183\5N(\5\u0182\u017f\3\2\2\2\u0183\u0186")
        buf.write("\3\2\2\2\u0184\u0182\3\2\2\2\u0184\u0185\3\2\2\2\u0185")
        buf.write("O\3\2\2\2\u0186\u0184\3\2\2\2\u0187\u0188\b)\1\2\u0188")
        buf.write("\u0189\5R*\2\u0189\u018f\3\2\2\2\u018a\u018b\f\4\2\2\u018b")
        buf.write("\u018c\t\6\2\2\u018c\u018e\5P)\5\u018d\u018a\3\2\2\2\u018e")
        buf.write("\u0191\3\2\2\2\u018f\u018d\3\2\2\2\u018f\u0190\3\2\2\2")
        buf.write("\u0190Q\3\2\2\2\u0191\u018f\3\2\2\2\u0192\u0193\b*\1\2")
        buf.write("\u0193\u0194\5T+\2\u0194\u019a\3\2\2\2\u0195\u0196\f\4")
        buf.write("\2\2\u0196\u0197\t\7\2\2\u0197\u0199\5T+\2\u0198\u0195")
        buf.write("\3\2\2\2\u0199\u019c\3\2\2\2\u019a\u0198\3\2\2\2\u019a")
        buf.write("\u019b\3\2\2\2\u019bS\3\2\2\2\u019c\u019a\3\2\2\2\u019d")
        buf.write("\u019e\b+\1\2\u019e\u019f\5V,\2\u019f\u01a5\3\2\2\2\u01a0")
        buf.write("\u01a1\f\4\2\2\u01a1\u01a2\t\b\2\2\u01a2\u01a4\5V,\2\u01a3")
        buf.write("\u01a0\3\2\2\2\u01a4\u01a7\3\2\2\2\u01a5\u01a3\3\2\2\2")
        buf.write("\u01a5\u01a6\3\2\2\2\u01a6U\3\2\2\2\u01a7\u01a5\3\2\2")
        buf.write("\2\u01a8\u01a9\b,\1\2\u01a9\u01aa\5X-\2\u01aa\u01b0\3")
        buf.write("\2\2\2\u01ab\u01ac\f\4\2\2\u01ac\u01ad\t\t\2\2\u01ad\u01af")
        buf.write("\5X-\2\u01ae\u01ab\3\2\2\2\u01af\u01b2\3\2\2\2\u01b0\u01ae")
        buf.write("\3\2\2\2\u01b0\u01b1\3\2\2\2\u01b1W\3\2\2\2\u01b2\u01b0")
        buf.write("\3\2\2\2\u01b3\u01b4\7*\2\2\u01b4\u01b7\5X-\2\u01b5\u01b7")
        buf.write("\5Z.\2\u01b6\u01b3\3\2\2\2\u01b6\u01b5\3\2\2\2\u01b7Y")
        buf.write("\3\2\2\2\u01b8\u01b9\7&\2\2\u01b9\u01bc\5Z.\2\u01ba\u01bc")
        buf.write("\5\\/\2\u01bb\u01b8\3\2\2\2\u01bb\u01ba\3\2\2\2\u01bc")
        buf.write("[\3\2\2\2\u01bd\u01be\b/\1\2\u01be\u01bf\5^\60\2\u01bf")
        buf.write("\u01cb\3\2\2\2\u01c0\u01c5\f\4\2\2\u01c1\u01c2\7\35\2")
        buf.write("\2\u01c2\u01c3\5N(\2\u01c3\u01c4\7\36\2\2\u01c4\u01c6")
        buf.write("\3\2\2\2\u01c5\u01c1\3\2\2\2\u01c6\u01c7\3\2\2\2\u01c7")
        buf.write("\u01c5\3\2\2\2\u01c7\u01c8\3\2\2\2\u01c8\u01ca\3\2\2\2")
        buf.write("\u01c9\u01c0\3\2\2\2\u01ca\u01cd\3\2\2\2\u01cb\u01c9\3")
        buf.write("\2\2\2\u01cb\u01cc\3\2\2\2\u01cc]\3\2\2\2\u01cd\u01cb")
        buf.write("\3\2\2\2\u01ce\u01cf\b\60\1\2\u01cf\u01d0\5`\61\2\u01d0")
        buf.write("\u01dd\3\2\2\2\u01d1\u01d2\f\4\2\2\u01d2\u01d3\7\37\2")
        buf.write("\2\u01d3\u01d9\7?\2\2\u01d4\u01d6\7\33\2\2\u01d5\u01d7")
        buf.write("\5f\64\2\u01d6\u01d5\3\2\2\2\u01d6\u01d7\3\2\2\2\u01d7")
        buf.write("\u01d8\3\2\2\2\u01d8\u01da\7\34\2\2\u01d9\u01d4\3\2\2")
        buf.write("\2\u01d9\u01da\3\2\2\2\u01da\u01dc\3\2\2\2\u01db\u01d1")
        buf.write("\3\2\2\2\u01dc\u01df\3\2\2\2\u01dd\u01db\3\2\2\2\u01dd")
        buf.write("\u01de\3\2\2\2\u01de_\3\2\2\2\u01df\u01dd\3\2\2\2\u01e0")
        buf.write("\u01e1\7?\2\2\u01e1\u01e2\7\66\2\2\u01e2\u01e8\7@\2\2")
        buf.write("\u01e3\u01e5\7\33\2\2\u01e4\u01e6\5f\64\2\u01e5\u01e4")
        buf.write("\3\2\2\2\u01e5\u01e6\3\2\2\2\u01e6\u01e7\3\2\2\2\u01e7")
        buf.write("\u01e9\7\34\2\2\u01e8\u01e3\3\2\2\2\u01e8\u01e9\3\2\2")
        buf.write("\2\u01e9\u01ec\3\2\2\2\u01ea\u01ec\5b\62\2\u01eb\u01e0")
        buf.write("\3\2\2\2\u01eb\u01ea\3\2\2\2\u01eca\3\2\2\2\u01ed\u01ee")
        buf.write("\7\31\2\2\u01ee\u01ef\7?\2\2\u01ef\u01f1\7\33\2\2\u01f0")
        buf.write("\u01f2\5f\64\2\u01f1\u01f0\3\2\2\2\u01f1\u01f2\3\2\2\2")
        buf.write("\u01f2\u01f3\3\2\2\2\u01f3\u01f6\7\34\2\2\u01f4\u01f6")
        buf.write("\5d\63\2\u01f5\u01ed\3\2\2\2\u01f5\u01f4\3\2\2\2\u01f6")
        buf.write("c\3\2\2\2\u01f7\u01f8\7\33\2\2\u01f8\u01f9\5N(\2\u01f9")
        buf.write("\u01fa\7\34\2\2\u01fa\u01fd\3\2\2\2\u01fb\u01fd\5h\65")
        buf.write("\2\u01fc\u01f7\3\2\2\2\u01fc\u01fb\3\2\2\2\u01fde\3\2")
        buf.write("\2\2\u01fe\u0203\5N(\2\u01ff\u0200\7 \2\2\u0200\u0202")
        buf.write("\5N(\2\u0201\u01ff\3\2\2\2\u0202\u0205\3\2\2\2\u0203\u0201")
        buf.write("\3\2\2\2\u0203\u0204\3\2\2\2\u0204g\3\2\2\2\u0205\u0203")
        buf.write("\3\2\2\2\u0206\u0210\7?\2\2\u0207\u0210\78\2\2\u0208\u0210")
        buf.write("\5p9\2\u0209\u0210\7=\2\2\u020a\u0210\7>\2\2\u020b\u0210")
        buf.write("\5r:\2\u020c\u0210\5j\66\2\u020d\u0210\7\26\2\2\u020e")
        buf.write("\u0210\7\22\2\2\u020f\u0206\3\2\2\2\u020f\u0207\3\2\2")
        buf.write("\2\u020f\u0208\3\2\2\2\u020f\u0209\3\2\2\2\u020f\u020a")
        buf.write("\3\2\2\2\u020f\u020b\3\2\2\2\u020f\u020c\3\2\2\2\u020f")
        buf.write("\u020d\3\2\2\2\u020f\u020e\3\2\2\2\u0210i\3\2\2\2\u0211")
        buf.write("\u0212\7\13\2\2\u0212\u0214\7\33\2\2\u0213\u0215\5l\67")
        buf.write("\2\u0214\u0213\3\2\2\2\u0214\u0215\3\2\2\2\u0215\u0216")
        buf.write("\3\2\2\2\u0216\u0217\7\34\2\2\u0217k\3\2\2\2\u0218\u021d")
        buf.write("\5n8\2\u0219\u021a\7 \2\2\u021a\u021c\5n8\2\u021b\u0219")
        buf.write("\3\2\2\2\u021c\u021f\3\2\2\2\u021d\u021b\3\2\2\2\u021d")
        buf.write("\u021e\3\2\2\2\u021em\3\2\2\2\u021f\u021d\3\2\2\2\u0220")
        buf.write("\u0223\5N(\2\u0221\u0223\5j\66\2\u0222\u0220\3\2\2\2\u0222")
        buf.write("\u0221\3\2\2\2\u0223o\3\2\2\2\u0224\u0225\t\n\2\2\u0225")
        buf.write("q\3\2\2\2\u0226\u0227\t\13\2\2\u0227s\3\2\2\2\64w\177")
        buf.write("\u0087\u0089\u008f\u00a1\u00ac\u00b4\u00b9\u00c0\u00c6")
        buf.write("\u00cf\u00db\u00e9\u00f7\u00fc\u010e\u0119\u0123\u012d")
        buf.write("\u0139\u013e\u014e\u015b\u0164\u016e\u0177\u0184\u018f")
        buf.write("\u019a\u01a5\u01b0\u01b6\u01bb\u01c7\u01cb\u01d6\u01d9")
        buf.write("\u01dd\u01e5\u01e8\u01eb\u01f1\u01f5\u01fc\u0203\u020f")
        buf.write("\u0214\u021d\u0222")
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
                      "DOUBLECOLON", "DOUBLEDOT", "ZERO", "DECINT", "OCTINT", 
                      "HEXINT", "BIINT", "FLOATLIT", "STRINGLIT", "ID", 
                      "DOLLAR_ID", "COMMENT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_classDeclaration = 1
    RULE_classBody = 2
    RULE_attrDeclaration = 3
    RULE_attrWithAssign = 4
    RULE_attrPair = 5
    RULE_attrWithoutAssign = 6
    RULE_attrList = 7
    RULE_identifier = 8
    RULE_typeName = 9
    RULE_methodDeclaration = 10
    RULE_paraList = 11
    RULE_paraDeclaration = 12
    RULE_idList = 13
    RULE_primitiveType = 14
    RULE_arrayType = 15
    RULE_elementType = 16
    RULE_classType = 17
    RULE_stmt = 18
    RULE_declarationStmt = 19
    RULE_declarationWithAssign = 20
    RULE_declarationPair = 21
    RULE_declarationWithoutAssign = 22
    RULE_varList = 23
    RULE_assignStmt = 24
    RULE_assignLHS = 25
    RULE_scalar = 26
    RULE_indexOperation = 27
    RULE_indexHead = 28
    RULE_ifStmt = 29
    RULE_ifBody = 30
    RULE_forInStmt = 31
    RULE_breakStmt = 32
    RULE_continueStmt = 33
    RULE_returnStmt = 34
    RULE_instanceCall = 35
    RULE_staticCall = 36
    RULE_blockStmt = 37
    RULE_exp = 38
    RULE_exp1 = 39
    RULE_exp2 = 40
    RULE_exp3 = 41
    RULE_exp4 = 42
    RULE_exp5 = 43
    RULE_exp6 = 44
    RULE_exp7 = 45
    RULE_exp8 = 46
    RULE_exp9 = 47
    RULE_exp10 = 48
    RULE_exp11 = 49
    RULE_expList = 50
    RULE_operand = 51
    RULE_indexArray = 52
    RULE_arrayBody = 53
    RULE_arrayLit = 54
    RULE_intLit = 55
    RULE_booleanLit = 56

    ruleNames =  [ "program", "classDeclaration", "classBody", "attrDeclaration", 
                   "attrWithAssign", "attrPair", "attrWithoutAssign", "attrList", 
                   "identifier", "typeName", "methodDeclaration", "paraList", 
                   "paraDeclaration", "idList", "primitiveType", "arrayType", 
                   "elementType", "classType", "stmt", "declarationStmt", 
                   "declarationWithAssign", "declarationPair", "declarationWithoutAssign", 
                   "varList", "assignStmt", "assignLHS", "scalar", "indexOperation", 
                   "indexHead", "ifStmt", "ifBody", "forInStmt", "breakStmt", 
                   "continueStmt", "returnStmt", "instanceCall", "staticCall", 
                   "blockStmt", "exp", "exp1", "exp2", "exp3", "exp4", "exp5", 
                   "exp6", "exp7", "exp8", "exp9", "exp10", "exp11", "expList", 
                   "operand", "indexArray", "arrayBody", "arrayLit", "intLit", 
                   "booleanLit" ]

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
    DECINT=55
    OCTINT=56
    HEXINT=57
    BIINT=58
    FLOATLIT=59
    STRINGLIT=60
    ID=61
    DOLLAR_ID=62
    COMMENT=63
    WS=64
    ERROR_CHAR=65
    UNCLOSE_STRING=66
    ILLEGAL_ESCAPE=67

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
            self.state = 115 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 114
                self.classDeclaration()
                self.state = 117 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==D96Parser.CLASS):
                    break

            self.state = 119
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
            self.state = 121
            self.match(D96Parser.CLASS)
            self.state = 122
            self.match(D96Parser.ID)
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COLON:
                self.state = 123
                self.match(D96Parser.COLON)
                self.state = 124
                self.match(D96Parser.ID)


            self.state = 127
            self.match(D96Parser.LP)
            self.state = 128
            self.classBody()
            self.state = 129
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
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.CONSTRUCTOR) | (1 << D96Parser.DESTRUCTOR) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLAR_ID))) != 0):
                self.state = 133
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.VAL, D96Parser.VAR]:
                    self.state = 131
                    self.attrDeclaration()
                    pass
                elif token in [D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.ID, D96Parser.DOLLAR_ID]:
                    self.state = 132
                    self.methodDeclaration()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 137
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

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def attrWithAssign(self):
            return self.getTypedRuleContext(D96Parser.AttrWithAssignContext,0)


        def attrWithoutAssign(self):
            return self.getTypedRuleContext(D96Parser.AttrWithoutAssignContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_attrDeclaration




    def attrDeclaration(self):

        localctx = D96Parser.AttrDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_attrDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 141
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 139
                self.attrWithAssign()
                pass

            elif la_ == 2:
                self.state = 140
                self.attrWithoutAssign()
                pass


            self.state = 143
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttrWithAssignContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(D96Parser.IdentifierContext,0)


        def attrPair(self):
            return self.getTypedRuleContext(D96Parser.AttrPairContext,0)


        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_attrWithAssign




    def attrWithAssign(self):

        localctx = D96Parser.AttrWithAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_attrWithAssign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.identifier()
            self.state = 146
            self.attrPair()
            self.state = 147
            self.exp(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttrPairContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def identifier(self):
            return self.getTypedRuleContext(D96Parser.IdentifierContext,0)


        def attrPair(self):
            return self.getTypedRuleContext(D96Parser.AttrPairContext,0)


        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def typeName(self):
            return self.getTypedRuleContext(D96Parser.TypeNameContext,0)


        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_attrPair




    def attrPair(self):

        localctx = D96Parser.AttrPairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_attrPair)
        try:
            self.state = 159
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                self.match(D96Parser.COMMA)
                self.state = 150
                self.identifier()
                self.state = 151
                self.attrPair()
                self.state = 152
                self.exp(0)
                self.state = 153
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 155
                self.match(D96Parser.COLON)
                self.state = 156
                self.typeName()
                self.state = 157
                self.match(D96Parser.ASSIGN)
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


    class AttrWithoutAssignContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attrList(self):
            return self.getTypedRuleContext(D96Parser.AttrListContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def typeName(self):
            return self.getTypedRuleContext(D96Parser.TypeNameContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_attrWithoutAssign




    def attrWithoutAssign(self):

        localctx = D96Parser.AttrWithoutAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_attrWithoutAssign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.attrList()
            self.state = 162
            self.match(D96Parser.COLON)
            self.state = 163
            self.typeName()
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
        self.enterRule(localctx, 14, self.RULE_attrList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.identifier()
            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 166
                self.match(D96Parser.COMMA)
                self.state = 167
                self.identifier()
                self.state = 172
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
        self.enterRule(localctx, 16, self.RULE_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
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
        self.enterRule(localctx, 18, self.RULE_typeName)
        try:
            self.state = 178
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 175
                self.primitiveType()
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 176
                self.arrayType()
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 177
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
        self.enterRule(localctx, 20, self.RULE_methodDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID, D96Parser.DOLLAR_ID]:
                self.state = 180
                self.identifier()
                self.state = 181
                self.match(D96Parser.LB)
                self.state = 183
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.ID:
                    self.state = 182
                    self.paraList()


                self.state = 185
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.CONSTRUCTOR]:
                self.state = 187
                self.match(D96Parser.CONSTRUCTOR)
                self.state = 188
                self.match(D96Parser.LB)
                self.state = 190
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.ID:
                    self.state = 189
                    self.paraList()


                self.state = 192
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.DESTRUCTOR]:
                self.state = 193
                self.match(D96Parser.DESTRUCTOR)
                self.state = 194
                self.match(D96Parser.LB)
                self.state = 195
                self.match(D96Parser.RB)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 198
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
        self.enterRule(localctx, 22, self.RULE_paraList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.paraDeclaration()
            self.state = 205
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.SEMI:
                self.state = 201
                self.match(D96Parser.SEMI)
                self.state = 202
                self.paraDeclaration()
                self.state = 207
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
        self.enterRule(localctx, 24, self.RULE_paraDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.idList()
            self.state = 209
            self.match(D96Parser.COLON)
            self.state = 210
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
        self.enterRule(localctx, 26, self.RULE_idList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.match(D96Parser.ID)
            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 213
                self.match(D96Parser.COMMA)
                self.state = 214
                self.match(D96Parser.ID)
                self.state = 219
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
        self.enterRule(localctx, 28, self.RULE_primitiveType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
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

        def intLit(self):
            return self.getTypedRuleContext(D96Parser.IntLitContext,0)


        def RS(self):
            return self.getToken(D96Parser.RS, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_arrayType




    def arrayType(self):

        localctx = D96Parser.ArrayTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_arrayType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.match(D96Parser.ARRAY)
            self.state = 223
            self.match(D96Parser.LS)
            self.state = 224
            self.elementType()
            self.state = 225
            self.match(D96Parser.COMMA)
            self.state = 226
            self.intLit()
            self.state = 227
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
        self.enterRule(localctx, 32, self.RULE_elementType)
        try:
            self.state = 231
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 229
                self.primitiveType()
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 230
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
        self.enterRule(localctx, 34, self.RULE_classType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
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


        def declarationStmt(self):
            return self.getTypedRuleContext(D96Parser.DeclarationStmtContext,0)


        def blockStmt(self):
            return self.getTypedRuleContext(D96Parser.BlockStmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_stmt




    def stmt(self):

        localctx = D96Parser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_stmt)
        try:
            self.state = 245
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 235
                self.assignStmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 236
                self.ifStmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 237
                self.forInStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 238
                self.breakStmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 239
                self.continueStmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 240
                self.returnStmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 241
                self.instanceCall()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 242
                self.staticCall()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 243
                self.declarationStmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 244
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

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def declarationWithAssign(self):
            return self.getTypedRuleContext(D96Parser.DeclarationWithAssignContext,0)


        def declarationWithoutAssign(self):
            return self.getTypedRuleContext(D96Parser.DeclarationWithoutAssignContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_declarationStmt




    def declarationStmt(self):

        localctx = D96Parser.DeclarationStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_declarationStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 250
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 248
                self.declarationWithAssign()
                pass

            elif la_ == 2:
                self.state = 249
                self.declarationWithoutAssign()
                pass


            self.state = 252
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationWithAssignContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def declarationPair(self):
            return self.getTypedRuleContext(D96Parser.DeclarationPairContext,0)


        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_declarationWithAssign




    def declarationWithAssign(self):

        localctx = D96Parser.DeclarationWithAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_declarationWithAssign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.match(D96Parser.ID)
            self.state = 255
            self.declarationPair()
            self.state = 256
            self.exp(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationPairContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def declarationPair(self):
            return self.getTypedRuleContext(D96Parser.DeclarationPairContext,0)


        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def typeName(self):
            return self.getTypedRuleContext(D96Parser.TypeNameContext,0)


        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_declarationPair




    def declarationPair(self):

        localctx = D96Parser.DeclarationPairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_declarationPair)
        try:
            self.state = 268
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 258
                self.match(D96Parser.COMMA)
                self.state = 259
                self.match(D96Parser.ID)
                self.state = 260
                self.declarationPair()
                self.state = 261
                self.exp(0)
                self.state = 262
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 264
                self.match(D96Parser.COLON)
                self.state = 265
                self.typeName()
                self.state = 266
                self.match(D96Parser.ASSIGN)
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


    class DeclarationWithoutAssignContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varList(self):
            return self.getTypedRuleContext(D96Parser.VarListContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def typeName(self):
            return self.getTypedRuleContext(D96Parser.TypeNameContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_declarationWithoutAssign




    def declarationWithoutAssign(self):

        localctx = D96Parser.DeclarationWithoutAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_declarationWithoutAssign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.varList()
            self.state = 271
            self.match(D96Parser.COLON)
            self.state = 272
            self.typeName()
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
        self.enterRule(localctx, 46, self.RULE_varList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.match(D96Parser.ID)
            self.state = 279
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 275
                self.match(D96Parser.COMMA)
                self.state = 276
                self.match(D96Parser.ID)
                self.state = 281
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
        self.enterRule(localctx, 48, self.RULE_assignStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.assignLHS()
            self.state = 283
            self.match(D96Parser.ASSIGN)
            self.state = 284
            self.exp(0)
            self.state = 285
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
        self.enterRule(localctx, 50, self.RULE_assignLHS)
        try:
            self.state = 289
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 287
                self.indexOperation()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 288
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
        self.enterRule(localctx, 52, self.RULE_scalar)
        try:
            self.state = 299
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 291
                self.exp(0)
                self.state = 292
                self.match(D96Parser.DOT)
                self.state = 293
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 295
                self.match(D96Parser.ID)
                self.state = 296
                self.match(D96Parser.DOUBLECOLON)
                self.state = 297
                self.match(D96Parser.DOLLAR_ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 298
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

        def exp7(self):
            return self.getTypedRuleContext(D96Parser.Exp7Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_indexOperation




    def indexOperation(self):

        localctx = D96Parser.IndexOperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_indexOperation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.exp7(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexHeadContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_indexHead




    def indexHead(self):

        localctx = D96Parser.IndexHeadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_indexHead)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.exp(0)
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
        self.enterRule(localctx, 58, self.RULE_ifStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.match(D96Parser.IF)
            self.state = 306
            self.ifBody()
            self.state = 311
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.ELSEIF:
                self.state = 307
                self.match(D96Parser.ELSEIF)
                self.state = 308
                self.ifBody()
                self.state = 313
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 316
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ELSE:
                self.state = 314
                self.match(D96Parser.ELSE)
                self.state = 315
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
        self.enterRule(localctx, 60, self.RULE_ifBody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.match(D96Parser.LB)
            self.state = 319
            self.exp(0)
            self.state = 320
            self.match(D96Parser.RB)
            self.state = 321
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
        self.enterRule(localctx, 62, self.RULE_forInStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            self.match(D96Parser.FOREACH)
            self.state = 324
            self.match(D96Parser.LB)
            self.state = 325
            self.scalar()
            self.state = 326
            self.match(D96Parser.IN)
            self.state = 327
            self.exp(0)
            self.state = 328
            self.match(D96Parser.DOUBLEDOT)
            self.state = 329
            self.exp(0)
            self.state = 332
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.BY:
                self.state = 330
                self.match(D96Parser.BY)
                self.state = 331
                self.exp(0)


            self.state = 334
            self.match(D96Parser.RB)
            self.state = 335
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
        self.enterRule(localctx, 64, self.RULE_breakStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.match(D96Parser.BREAK)
            self.state = 338
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
        self.enterRule(localctx, 66, self.RULE_continueStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self.match(D96Parser.CONTINUE)
            self.state = 341
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
        self.enterRule(localctx, 68, self.RULE_returnStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self.match(D96Parser.RETURN)
            self.state = 345
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.LB) | (1 << D96Parser.MINUS) | (1 << D96Parser.NOT) | (1 << D96Parser.ZERO) | (1 << D96Parser.DECINT) | (1 << D96Parser.OCTINT) | (1 << D96Parser.HEXINT) | (1 << D96Parser.BIINT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.STRINGLIT) | (1 << D96Parser.ID))) != 0):
                self.state = 344
                self.exp(0)


            self.state = 347
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
        self.enterRule(localctx, 70, self.RULE_instanceCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            self.exp(0)
            self.state = 350
            self.match(D96Parser.DOT)
            self.state = 351
            self.match(D96Parser.ID)
            self.state = 352
            self.match(D96Parser.LB)
            self.state = 354
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.LB) | (1 << D96Parser.MINUS) | (1 << D96Parser.NOT) | (1 << D96Parser.ZERO) | (1 << D96Parser.DECINT) | (1 << D96Parser.OCTINT) | (1 << D96Parser.HEXINT) | (1 << D96Parser.BIINT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.STRINGLIT) | (1 << D96Parser.ID))) != 0):
                self.state = 353
                self.expList()


            self.state = 356
            self.match(D96Parser.RB)
            self.state = 357
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
        self.enterRule(localctx, 72, self.RULE_staticCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.match(D96Parser.ID)
            self.state = 360
            self.match(D96Parser.DOUBLECOLON)
            self.state = 361
            self.match(D96Parser.DOLLAR_ID)
            self.state = 362
            self.match(D96Parser.LB)
            self.state = 364
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.LB) | (1 << D96Parser.MINUS) | (1 << D96Parser.NOT) | (1 << D96Parser.ZERO) | (1 << D96Parser.DECINT) | (1 << D96Parser.OCTINT) | (1 << D96Parser.HEXINT) | (1 << D96Parser.BIINT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.STRINGLIT) | (1 << D96Parser.ID))) != 0):
                self.state = 363
                self.expList()


            self.state = 366
            self.match(D96Parser.RB)
            self.state = 367
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

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.StmtContext)
            else:
                return self.getTypedRuleContext(D96Parser.StmtContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_blockStmt




    def blockStmt(self):

        localctx = D96Parser.BlockStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_blockStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
            self.match(D96Parser.LP)
            self.state = 373
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.BREAK) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.IF) | (1 << D96Parser.FOREACH) | (1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.ARRAY) | (1 << D96Parser.RETURN) | (1 << D96Parser.NULL) | (1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.LB) | (1 << D96Parser.LP) | (1 << D96Parser.MINUS) | (1 << D96Parser.NOT) | (1 << D96Parser.ZERO) | (1 << D96Parser.DECINT) | (1 << D96Parser.OCTINT) | (1 << D96Parser.HEXINT) | (1 << D96Parser.BIINT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.STRINGLIT) | (1 << D96Parser.ID))) != 0):
                self.state = 370
                self.stmt()
                self.state = 375
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 376
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
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_exp, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
            self.exp1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 386
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.ExpContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                    self.state = 381
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 382
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.STREQ or _la==D96Parser.STRADD):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 383
                    self.exp(3) 
                self.state = 388
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

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
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_exp1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 390
            self.exp2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 397
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                    self.state = 392
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 393
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.EQUAL) | (1 << D96Parser.DIFF) | (1 << D96Parser.GT) | (1 << D96Parser.GTE) | (1 << D96Parser.LT) | (1 << D96Parser.LTE))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 394
                    self.exp1(3) 
                self.state = 399
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

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
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_exp2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 408
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 403
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 404
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.AND or _la==D96Parser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 405
                    self.exp3(0) 
                self.state = 410
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

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
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_exp3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 412
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 419
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 414
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 415
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ADD or _la==D96Parser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 416
                    self.exp4(0) 
                self.state = 421
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

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
        _startState = 84
        self.enterRecursionRule(localctx, 84, self.RULE_exp4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 423
            self.exp5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 430
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                    self.state = 425
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 426
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.MUL) | (1 << D96Parser.DIV) | (1 << D96Parser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 427
                    self.exp5() 
                self.state = 432
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

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
        self.enterRule(localctx, 86, self.RULE_exp5)
        try:
            self.state = 436
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 433
                self.match(D96Parser.NOT)
                self.state = 434
                self.exp5()
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.SELF, D96Parser.NEW, D96Parser.LB, D96Parser.MINUS, D96Parser.ZERO, D96Parser.DECINT, D96Parser.OCTINT, D96Parser.HEXINT, D96Parser.BIINT, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 435
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
        self.enterRule(localctx, 88, self.RULE_exp6)
        try:
            self.state = 441
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 438
                self.match(D96Parser.MINUS)
                self.state = 439
                self.exp6()
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.SELF, D96Parser.NEW, D96Parser.LB, D96Parser.ZERO, D96Parser.DECINT, D96Parser.OCTINT, D96Parser.HEXINT, D96Parser.BIINT, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 440
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
        _startState = 90
        self.enterRecursionRule(localctx, 90, self.RULE_exp7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 444
            self.exp8(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 457
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp7)
                    self.state = 446
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 451 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 447
                            self.match(D96Parser.LS)
                            self.state = 448
                            self.exp(0)
                            self.state = 449
                            self.match(D96Parser.RS)

                        else:
                            raise NoViableAltException(self)
                        self.state = 453 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
             
                self.state = 459
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

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
        _startState = 92
        self.enterRecursionRule(localctx, 92, self.RULE_exp8, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 461
            self.exp9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 475
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp8)
                    self.state = 463
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 464
                    self.match(D96Parser.DOT)
                    self.state = 465
                    self.match(D96Parser.ID)
                    self.state = 471
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
                    if la_ == 1:
                        self.state = 466
                        self.match(D96Parser.LB)
                        self.state = 468
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.LB) | (1 << D96Parser.MINUS) | (1 << D96Parser.NOT) | (1 << D96Parser.ZERO) | (1 << D96Parser.DECINT) | (1 << D96Parser.OCTINT) | (1 << D96Parser.HEXINT) | (1 << D96Parser.BIINT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.STRINGLIT) | (1 << D96Parser.ID))) != 0):
                            self.state = 467
                            self.expList()


                        self.state = 470
                        self.match(D96Parser.RB)

             
                self.state = 477
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

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
        self.enterRule(localctx, 94, self.RULE_exp9)
        self._la = 0 # Token type
        try:
            self.state = 489
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 478
                self.match(D96Parser.ID)
                self.state = 479
                self.match(D96Parser.DOUBLECOLON)
                self.state = 480
                self.match(D96Parser.DOLLAR_ID)
                self.state = 486
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
                if la_ == 1:
                    self.state = 481
                    self.match(D96Parser.LB)
                    self.state = 483
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.LB) | (1 << D96Parser.MINUS) | (1 << D96Parser.NOT) | (1 << D96Parser.ZERO) | (1 << D96Parser.DECINT) | (1 << D96Parser.OCTINT) | (1 << D96Parser.HEXINT) | (1 << D96Parser.BIINT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.STRINGLIT) | (1 << D96Parser.ID))) != 0):
                        self.state = 482
                        self.expList()


                    self.state = 485
                    self.match(D96Parser.RB)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 488
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
        self.enterRule(localctx, 96, self.RULE_exp10)
        self._la = 0 # Token type
        try:
            self.state = 499
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 491
                self.match(D96Parser.NEW)
                self.state = 492
                self.match(D96Parser.ID)
                self.state = 493
                self.match(D96Parser.LB)
                self.state = 495
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.LB) | (1 << D96Parser.MINUS) | (1 << D96Parser.NOT) | (1 << D96Parser.ZERO) | (1 << D96Parser.DECINT) | (1 << D96Parser.OCTINT) | (1 << D96Parser.HEXINT) | (1 << D96Parser.BIINT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.STRINGLIT) | (1 << D96Parser.ID))) != 0):
                    self.state = 494
                    self.expList()


                self.state = 497
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.SELF, D96Parser.LB, D96Parser.ZERO, D96Parser.DECINT, D96Parser.OCTINT, D96Parser.HEXINT, D96Parser.BIINT, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 498
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
        self.enterRule(localctx, 98, self.RULE_exp11)
        try:
            self.state = 506
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 501
                self.match(D96Parser.LB)
                self.state = 502
                self.exp(0)
                self.state = 503
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.SELF, D96Parser.ZERO, D96Parser.DECINT, D96Parser.OCTINT, D96Parser.HEXINT, D96Parser.BIINT, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 505
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
        self.enterRule(localctx, 100, self.RULE_expList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 508
            self.exp(0)
            self.state = 513
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 509
                self.match(D96Parser.COMMA)
                self.state = 510
                self.exp(0)
                self.state = 515
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

        def intLit(self):
            return self.getTypedRuleContext(D96Parser.IntLitContext,0)


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
        self.enterRule(localctx, 102, self.RULE_operand)
        try:
            self.state = 525
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 516
                self.match(D96Parser.ID)
                pass
            elif token in [D96Parser.ZERO]:
                self.enterOuterAlt(localctx, 2)
                self.state = 517
                self.match(D96Parser.ZERO)
                pass
            elif token in [D96Parser.DECINT, D96Parser.OCTINT, D96Parser.HEXINT, D96Parser.BIINT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 518
                self.intLit()
                pass
            elif token in [D96Parser.FLOATLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 519
                self.match(D96Parser.FLOATLIT)
                pass
            elif token in [D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 520
                self.match(D96Parser.STRINGLIT)
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE]:
                self.enterOuterAlt(localctx, 6)
                self.state = 521
                self.booleanLit()
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 7)
                self.state = 522
                self.indexArray()
                pass
            elif token in [D96Parser.SELF]:
                self.enterOuterAlt(localctx, 8)
                self.state = 523
                self.match(D96Parser.SELF)
                pass
            elif token in [D96Parser.NULL]:
                self.enterOuterAlt(localctx, 9)
                self.state = 524
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
        self.enterRule(localctx, 104, self.RULE_indexArray)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 527
            self.match(D96Parser.ARRAY)
            self.state = 528
            self.match(D96Parser.LB)
            self.state = 530
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.LB) | (1 << D96Parser.MINUS) | (1 << D96Parser.NOT) | (1 << D96Parser.ZERO) | (1 << D96Parser.DECINT) | (1 << D96Parser.OCTINT) | (1 << D96Parser.HEXINT) | (1 << D96Parser.BIINT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.STRINGLIT) | (1 << D96Parser.ID))) != 0):
                self.state = 529
                self.arrayBody()


            self.state = 532
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
        self.enterRule(localctx, 106, self.RULE_arrayBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 534
            self.arrayLit()
            self.state = 539
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 535
                self.match(D96Parser.COMMA)
                self.state = 536
                self.arrayLit()
                self.state = 541
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
        self.enterRule(localctx, 108, self.RULE_arrayLit)
        try:
            self.state = 544
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 542
                self.exp(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 543
                self.indexArray()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntLitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DECINT(self):
            return self.getToken(D96Parser.DECINT, 0)

        def OCTINT(self):
            return self.getToken(D96Parser.OCTINT, 0)

        def HEXINT(self):
            return self.getToken(D96Parser.HEXINT, 0)

        def BIINT(self):
            return self.getToken(D96Parser.BIINT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_intLit




    def intLit(self):

        localctx = D96Parser.IntLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_intLit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 546
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.DECINT) | (1 << D96Parser.OCTINT) | (1 << D96Parser.HEXINT) | (1 << D96Parser.BIINT))) != 0)):
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
        self.enterRule(localctx, 112, self.RULE_booleanLit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 548
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
        self._predicates[38] = self.exp_sempred
        self._predicates[39] = self.exp1_sempred
        self._predicates[40] = self.exp2_sempred
        self._predicates[41] = self.exp3_sempred
        self._predicates[42] = self.exp4_sempred
        self._predicates[45] = self.exp7_sempred
        self._predicates[46] = self.exp8_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp_sempred(self, localctx:ExpContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def exp1_sempred(self, localctx:Exp1Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def exp4_sempred(self, localctx:Exp4Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def exp7_sempred(self, localctx:Exp7Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

    def exp8_sempred(self, localctx:Exp8Context, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         




