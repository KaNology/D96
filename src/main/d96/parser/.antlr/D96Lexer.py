# Generated from c:\Users\ADMIN\Desktop\assignment2\src\main\d96\parser\D96.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2E")
        buf.write("\u0224\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3")
        buf.write("\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3")
        buf.write("\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3\33")
        buf.write("\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3")
        buf.write("!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)")
        buf.write("\3)\3*\3*\3*\3+\3+\3+\3,\3,\3,\3-\3-\3.\3.\3.\3/\3/\3")
        buf.write("\60\3\60\3\60\3\61\3\61\3\62\3\62\3\62\3\63\3\63\3\63")
        buf.write("\3\63\3\64\3\64\3\64\3\65\3\65\3\65\3\66\3\66\3\66\3\67")
        buf.write("\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\5\67\u0172\n")
        buf.write("\67\38\38\58\u0176\n8\38\78\u0179\n8\f8\168\u017c\138")
        buf.write("\38\38\39\39\39\59\u0183\n9\39\79\u0186\n9\f9\169\u0189")
        buf.write("\139\39\39\3:\3:\3:\3:\5:\u0191\n:\3:\7:\u0194\n:\f:\16")
        buf.write(":\u0197\13:\3:\3:\3;\3;\3;\3;\5;\u019f\n;\3;\7;\u01a2")
        buf.write("\n;\f;\16;\u01a5\13;\3;\3;\3<\3<\5<\u01ab\n<\3<\3<\3<")
        buf.write("\3<\3<\3<\3<\3<\5<\u01b5\n<\3<\3<\3=\3=\5=\u01bb\n=\3")
        buf.write("=\7=\u01be\n=\f=\16=\u01c1\13=\3>\3>\7>\u01c5\n>\f>\16")
        buf.write(">\u01c8\13>\3?\3?\5?\u01cc\n?\3?\6?\u01cf\n?\r?\16?\u01d0")
        buf.write("\3@\3@\7@\u01d5\n@\f@\16@\u01d8\13@\3@\3@\3@\3A\3A\3A")
        buf.write("\3A\5A\u01e1\nA\3B\3B\3B\3C\3C\7C\u01e8\nC\fC\16C\u01eb")
        buf.write("\13C\3D\3D\6D\u01ef\nD\rD\16D\u01f0\3E\3E\3E\3E\7E\u01f7")
        buf.write("\nE\fE\16E\u01fa\13E\3E\3E\3E\3E\3E\3F\6F\u0202\nF\rF")
        buf.write("\16F\u0203\3F\3F\3G\3G\3G\3H\3H\7H\u020d\nH\fH\16H\u0210")
        buf.write("\13H\3H\5H\u0213\nH\3H\3H\3I\3I\7I\u0219\nI\fI\16I\u021c")
        buf.write("\13I\3I\3I\3I\5I\u0221\nI\3I\3I\3\u01f8\2J\3\3\5\4\7\5")
        buf.write("\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35")
        buf.write("\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33")
        buf.write("\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[")
        buf.write("/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=y\2{\2}\2")
        buf.write("\177>\u0081\2\u0083\2\u0085?\u0087@\u0089A\u008bB\u008d")
        buf.write("C\u008fD\u0091E\3\2\25\4\2ZZzz\4\2DDdd\3\2\63;\3\2\62")
        buf.write(";\3\2\639\3\2\629\4\2\63;CH\4\2\62;CH\3\2\63\63\3\2\62")
        buf.write("\63\4\2GGgg\4\2--//\6\2\n\f\16\17$$^^\t\2))^^ddhhpptt")
        buf.write("vv\5\2C\\aac|\6\2\62;C\\aac|\5\2\n\f\16\17\"\"\7\3\n\f")
        buf.write("\16\17$$))^^\3\2^^\2\u023b\2\3\3\2\2\2\2\5\3\2\2\2\2\7")
        buf.write("\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2")
        buf.write("\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2")
        buf.write("\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2")
        buf.write("\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2")
        buf.write("\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y")
        buf.write("\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2")
        buf.write("c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2")
        buf.write("\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2")
        buf.write("\2\2w\3\2\2\2\2\177\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3")
        buf.write("\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2")
        buf.write("\2\u008f\3\2\2\2\2\u0091\3\2\2\2\3\u0093\3\2\2\2\5\u0099")
        buf.write("\3\2\2\2\7\u00a2\3\2\2\2\t\u00a5\3\2\2\2\13\u00ac\3\2")
        buf.write("\2\2\r\u00b1\3\2\2\2\17\u00b9\3\2\2\2\21\u00be\3\2\2\2")
        buf.write("\23\u00c4\3\2\2\2\25\u00ca\3\2\2\2\27\u00cd\3\2\2\2\31")
        buf.write("\u00d1\3\2\2\2\33\u00d7\3\2\2\2\35\u00df\3\2\2\2\37\u00e6")
        buf.write("\3\2\2\2!\u00ed\3\2\2\2#\u00f2\3\2\2\2%\u00f8\3\2\2\2")
        buf.write("\'\u00fc\3\2\2\2)\u0100\3\2\2\2+\u0105\3\2\2\2-\u0111")
        buf.write("\3\2\2\2/\u011c\3\2\2\2\61\u0120\3\2\2\2\63\u0123\3\2")
        buf.write("\2\2\65\u0125\3\2\2\2\67\u0127\3\2\2\29\u0129\3\2\2\2")
        buf.write(";\u012b\3\2\2\2=\u012d\3\2\2\2?\u012f\3\2\2\2A\u0131\3")
        buf.write("\2\2\2C\u0133\3\2\2\2E\u0135\3\2\2\2G\u0137\3\2\2\2I\u0139")
        buf.write("\3\2\2\2K\u013b\3\2\2\2M\u013d\3\2\2\2O\u013f\3\2\2\2")
        buf.write("Q\u0141\3\2\2\2S\u0143\3\2\2\2U\u0146\3\2\2\2W\u0149\3")
        buf.write("\2\2\2Y\u014c\3\2\2\2[\u014e\3\2\2\2]\u0151\3\2\2\2_\u0153")
        buf.write("\3\2\2\2a\u0156\3\2\2\2c\u0158\3\2\2\2e\u015b\3\2\2\2")
        buf.write("g\u015f\3\2\2\2i\u0162\3\2\2\2k\u0165\3\2\2\2m\u0171\3")
        buf.write("\2\2\2o\u0173\3\2\2\2q\u017f\3\2\2\2s\u018c\3\2\2\2u\u019a")
        buf.write("\3\2\2\2w\u01b4\3\2\2\2y\u01b8\3\2\2\2{\u01c2\3\2\2\2")
        buf.write("}\u01c9\3\2\2\2\177\u01d2\3\2\2\2\u0081\u01e0\3\2\2\2")
        buf.write("\u0083\u01e2\3\2\2\2\u0085\u01e5\3\2\2\2\u0087\u01ec\3")
        buf.write("\2\2\2\u0089\u01f2\3\2\2\2\u008b\u0201\3\2\2\2\u008d\u0207")
        buf.write("\3\2\2\2\u008f\u020a\3\2\2\2\u0091\u0216\3\2\2\2\u0093")
        buf.write("\u0094\7D\2\2\u0094\u0095\7t\2\2\u0095\u0096\7g\2\2\u0096")
        buf.write("\u0097\7c\2\2\u0097\u0098\7m\2\2\u0098\4\3\2\2\2\u0099")
        buf.write("\u009a\7E\2\2\u009a\u009b\7q\2\2\u009b\u009c\7p\2\2\u009c")
        buf.write("\u009d\7v\2\2\u009d\u009e\7k\2\2\u009e\u009f\7p\2\2\u009f")
        buf.write("\u00a0\7w\2\2\u00a0\u00a1\7g\2\2\u00a1\6\3\2\2\2\u00a2")
        buf.write("\u00a3\7K\2\2\u00a3\u00a4\7h\2\2\u00a4\b\3\2\2\2\u00a5")
        buf.write("\u00a6\7G\2\2\u00a6\u00a7\7n\2\2\u00a7\u00a8\7u\2\2\u00a8")
        buf.write("\u00a9\7g\2\2\u00a9\u00aa\7k\2\2\u00aa\u00ab\7h\2\2\u00ab")
        buf.write("\n\3\2\2\2\u00ac\u00ad\7G\2\2\u00ad\u00ae\7n\2\2\u00ae")
        buf.write("\u00af\7u\2\2\u00af\u00b0\7g\2\2\u00b0\f\3\2\2\2\u00b1")
        buf.write("\u00b2\7H\2\2\u00b2\u00b3\7q\2\2\u00b3\u00b4\7t\2\2\u00b4")
        buf.write("\u00b5\7g\2\2\u00b5\u00b6\7c\2\2\u00b6\u00b7\7e\2\2\u00b7")
        buf.write("\u00b8\7j\2\2\u00b8\16\3\2\2\2\u00b9\u00ba\7V\2\2\u00ba")
        buf.write("\u00bb\7t\2\2\u00bb\u00bc\7w\2\2\u00bc\u00bd\7g\2\2\u00bd")
        buf.write("\20\3\2\2\2\u00be\u00bf\7H\2\2\u00bf\u00c0\7c\2\2\u00c0")
        buf.write("\u00c1\7n\2\2\u00c1\u00c2\7u\2\2\u00c2\u00c3\7g\2\2\u00c3")
        buf.write("\22\3\2\2\2\u00c4\u00c5\7C\2\2\u00c5\u00c6\7t\2\2\u00c6")
        buf.write("\u00c7\7t\2\2\u00c7\u00c8\7c\2\2\u00c8\u00c9\7{\2\2\u00c9")
        buf.write("\24\3\2\2\2\u00ca\u00cb\7K\2\2\u00cb\u00cc\7p\2\2\u00cc")
        buf.write("\26\3\2\2\2\u00cd\u00ce\7K\2\2\u00ce\u00cf\7p\2\2\u00cf")
        buf.write("\u00d0\7v\2\2\u00d0\30\3\2\2\2\u00d1\u00d2\7H\2\2\u00d2")
        buf.write("\u00d3\7n\2\2\u00d3\u00d4\7q\2\2\u00d4\u00d5\7c\2\2\u00d5")
        buf.write("\u00d6\7v\2\2\u00d6\32\3\2\2\2\u00d7\u00d8\7D\2\2\u00d8")
        buf.write("\u00d9\7q\2\2\u00d9\u00da\7q\2\2\u00da\u00db\7n\2\2\u00db")
        buf.write("\u00dc\7g\2\2\u00dc\u00dd\7c\2\2\u00dd\u00de\7p\2\2\u00de")
        buf.write("\34\3\2\2\2\u00df\u00e0\7U\2\2\u00e0\u00e1\7v\2\2\u00e1")
        buf.write("\u00e2\7t\2\2\u00e2\u00e3\7k\2\2\u00e3\u00e4\7p\2\2\u00e4")
        buf.write("\u00e5\7i\2\2\u00e5\36\3\2\2\2\u00e6\u00e7\7T\2\2\u00e7")
        buf.write("\u00e8\7g\2\2\u00e8\u00e9\7v\2\2\u00e9\u00ea\7w\2\2\u00ea")
        buf.write("\u00eb\7t\2\2\u00eb\u00ec\7p\2\2\u00ec \3\2\2\2\u00ed")
        buf.write("\u00ee\7P\2\2\u00ee\u00ef\7w\2\2\u00ef\u00f0\7n\2\2\u00f0")
        buf.write("\u00f1\7n\2\2\u00f1\"\3\2\2\2\u00f2\u00f3\7E\2\2\u00f3")
        buf.write("\u00f4\7n\2\2\u00f4\u00f5\7c\2\2\u00f5\u00f6\7u\2\2\u00f6")
        buf.write("\u00f7\7u\2\2\u00f7$\3\2\2\2\u00f8\u00f9\7X\2\2\u00f9")
        buf.write("\u00fa\7c\2\2\u00fa\u00fb\7n\2\2\u00fb&\3\2\2\2\u00fc")
        buf.write("\u00fd\7X\2\2\u00fd\u00fe\7c\2\2\u00fe\u00ff\7t\2\2\u00ff")
        buf.write("(\3\2\2\2\u0100\u0101\7U\2\2\u0101\u0102\7g\2\2\u0102")
        buf.write("\u0103\7n\2\2\u0103\u0104\7h\2\2\u0104*\3\2\2\2\u0105")
        buf.write("\u0106\7E\2\2\u0106\u0107\7q\2\2\u0107\u0108\7p\2\2\u0108")
        buf.write("\u0109\7u\2\2\u0109\u010a\7v\2\2\u010a\u010b\7t\2\2\u010b")
        buf.write("\u010c\7w\2\2\u010c\u010d\7e\2\2\u010d\u010e\7v\2\2\u010e")
        buf.write("\u010f\7q\2\2\u010f\u0110\7t\2\2\u0110,\3\2\2\2\u0111")
        buf.write("\u0112\7F\2\2\u0112\u0113\7g\2\2\u0113\u0114\7u\2\2\u0114")
        buf.write("\u0115\7v\2\2\u0115\u0116\7t\2\2\u0116\u0117\7w\2\2\u0117")
        buf.write("\u0118\7e\2\2\u0118\u0119\7v\2\2\u0119\u011a\7q\2\2\u011a")
        buf.write("\u011b\7t\2\2\u011b.\3\2\2\2\u011c\u011d\7P\2\2\u011d")
        buf.write("\u011e\7g\2\2\u011e\u011f\7y\2\2\u011f\60\3\2\2\2\u0120")
        buf.write("\u0121\7D\2\2\u0121\u0122\7{\2\2\u0122\62\3\2\2\2\u0123")
        buf.write("\u0124\7*\2\2\u0124\64\3\2\2\2\u0125\u0126\7+\2\2\u0126")
        buf.write("\66\3\2\2\2\u0127\u0128\7]\2\2\u01288\3\2\2\2\u0129\u012a")
        buf.write("\7_\2\2\u012a:\3\2\2\2\u012b\u012c\7\60\2\2\u012c<\3\2")
        buf.write("\2\2\u012d\u012e\7.\2\2\u012e>\3\2\2\2\u012f\u0130\7=")
        buf.write("\2\2\u0130@\3\2\2\2\u0131\u0132\7}\2\2\u0132B\3\2\2\2")
        buf.write("\u0133\u0134\7\177\2\2\u0134D\3\2\2\2\u0135\u0136\7<\2")
        buf.write("\2\u0136F\3\2\2\2\u0137\u0138\7-\2\2\u0138H\3\2\2\2\u0139")
        buf.write("\u013a\7/\2\2\u013aJ\3\2\2\2\u013b\u013c\7,\2\2\u013c")
        buf.write("L\3\2\2\2\u013d\u013e\7\61\2\2\u013eN\3\2\2\2\u013f\u0140")
        buf.write("\7\'\2\2\u0140P\3\2\2\2\u0141\u0142\7#\2\2\u0142R\3\2")
        buf.write("\2\2\u0143\u0144\7(\2\2\u0144\u0145\7(\2\2\u0145T\3\2")
        buf.write("\2\2\u0146\u0147\7~\2\2\u0147\u0148\7~\2\2\u0148V\3\2")
        buf.write("\2\2\u0149\u014a\7?\2\2\u014a\u014b\7?\2\2\u014bX\3\2")
        buf.write("\2\2\u014c\u014d\7?\2\2\u014dZ\3\2\2\2\u014e\u014f\7#")
        buf.write("\2\2\u014f\u0150\7?\2\2\u0150\\\3\2\2\2\u0151\u0152\7")
        buf.write("@\2\2\u0152^\3\2\2\2\u0153\u0154\7@\2\2\u0154\u0155\7")
        buf.write("?\2\2\u0155`\3\2\2\2\u0156\u0157\7>\2\2\u0157b\3\2\2\2")
        buf.write("\u0158\u0159\7>\2\2\u0159\u015a\7?\2\2\u015ad\3\2\2\2")
        buf.write("\u015b\u015c\7?\2\2\u015c\u015d\7?\2\2\u015d\u015e\7\60")
        buf.write("\2\2\u015ef\3\2\2\2\u015f\u0160\7-\2\2\u0160\u0161\7\60")
        buf.write("\2\2\u0161h\3\2\2\2\u0162\u0163\7<\2\2\u0163\u0164\7<")
        buf.write("\2\2\u0164j\3\2\2\2\u0165\u0166\7\60\2\2\u0166\u0167\7")
        buf.write("\60\2\2\u0167l\3\2\2\2\u0168\u0172\7\62\2\2\u0169\u016a")
        buf.write("\7\62\2\2\u016a\u0172\7\62\2\2\u016b\u016c\7\62\2\2\u016c")
        buf.write("\u016d\t\2\2\2\u016d\u0172\7\62\2\2\u016e\u016f\7\62\2")
        buf.write("\2\u016f\u0170\t\3\2\2\u0170\u0172\7\62\2\2\u0171\u0168")
        buf.write("\3\2\2\2\u0171\u0169\3\2\2\2\u0171\u016b\3\2\2\2\u0171")
        buf.write("\u016e\3\2\2\2\u0172n\3\2\2\2\u0173\u017a\t\4\2\2\u0174")
        buf.write("\u0176\7a\2\2\u0175\u0174\3\2\2\2\u0175\u0176\3\2\2\2")
        buf.write("\u0176\u0177\3\2\2\2\u0177\u0179\t\5\2\2\u0178\u0175\3")
        buf.write("\2\2\2\u0179\u017c\3\2\2\2\u017a\u0178\3\2\2\2\u017a\u017b")
        buf.write("\3\2\2\2\u017b\u017d\3\2\2\2\u017c\u017a\3\2\2\2\u017d")
        buf.write("\u017e\b8\2\2\u017ep\3\2\2\2\u017f\u0180\7\62\2\2\u0180")
        buf.write("\u0187\t\6\2\2\u0181\u0183\7a\2\2\u0182\u0181\3\2\2\2")
        buf.write("\u0182\u0183\3\2\2\2\u0183\u0184\3\2\2\2\u0184\u0186\t")
        buf.write("\7\2\2\u0185\u0182\3\2\2\2\u0186\u0189\3\2\2\2\u0187\u0185")
        buf.write("\3\2\2\2\u0187\u0188\3\2\2\2\u0188\u018a\3\2\2\2\u0189")
        buf.write("\u0187\3\2\2\2\u018a\u018b\b9\3\2\u018br\3\2\2\2\u018c")
        buf.write("\u018d\7\62\2\2\u018d\u018e\t\2\2\2\u018e\u0195\t\b\2")
        buf.write("\2\u018f\u0191\7a\2\2\u0190\u018f\3\2\2\2\u0190\u0191")
        buf.write("\3\2\2\2\u0191\u0192\3\2\2\2\u0192\u0194\t\t\2\2\u0193")
        buf.write("\u0190\3\2\2\2\u0194\u0197\3\2\2\2\u0195\u0193\3\2\2\2")
        buf.write("\u0195\u0196\3\2\2\2\u0196\u0198\3\2\2\2\u0197\u0195\3")
        buf.write("\2\2\2\u0198\u0199\b:\4\2\u0199t\3\2\2\2\u019a\u019b\7")
        buf.write("\62\2\2\u019b\u019c\t\3\2\2\u019c\u01a3\t\n\2\2\u019d")
        buf.write("\u019f\7a\2\2\u019e\u019d\3\2\2\2\u019e\u019f\3\2\2\2")
        buf.write("\u019f\u01a0\3\2\2\2\u01a0\u01a2\t\13\2\2\u01a1\u019e")
        buf.write("\3\2\2\2\u01a2\u01a5\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a3")
        buf.write("\u01a4\3\2\2\2\u01a4\u01a6\3\2\2\2\u01a5\u01a3\3\2\2\2")
        buf.write("\u01a6\u01a7\b;\5\2\u01a7v\3\2\2\2\u01a8\u01aa\5y=\2\u01a9")
        buf.write("\u01ab\5{>\2\u01aa\u01a9\3\2\2\2\u01aa\u01ab\3\2\2\2\u01ab")
        buf.write("\u01ac\3\2\2\2\u01ac\u01ad\5}?\2\u01ad\u01b5\3\2\2\2\u01ae")
        buf.write("\u01af\5y=\2\u01af\u01b0\5{>\2\u01b0\u01b5\3\2\2\2\u01b1")
        buf.write("\u01b2\5{>\2\u01b2\u01b3\5}?\2\u01b3\u01b5\3\2\2\2\u01b4")
        buf.write("\u01a8\3\2\2\2\u01b4\u01ae\3\2\2\2\u01b4\u01b1\3\2\2\2")
        buf.write("\u01b5\u01b6\3\2\2\2\u01b6\u01b7\b<\6\2\u01b7x\3\2\2\2")
        buf.write("\u01b8\u01bf\t\5\2\2\u01b9\u01bb\7a\2\2\u01ba\u01b9\3")
        buf.write("\2\2\2\u01ba\u01bb\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bc\u01be")
        buf.write("\t\5\2\2\u01bd\u01ba\3\2\2\2\u01be\u01c1\3\2\2\2\u01bf")
        buf.write("\u01bd\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0z\3\2\2\2\u01c1")
        buf.write("\u01bf\3\2\2\2\u01c2\u01c6\5;\36\2\u01c3\u01c5\t\5\2\2")
        buf.write("\u01c4\u01c3\3\2\2\2\u01c5\u01c8\3\2\2\2\u01c6\u01c4\3")
        buf.write("\2\2\2\u01c6\u01c7\3\2\2\2\u01c7|\3\2\2\2\u01c8\u01c6")
        buf.write("\3\2\2\2\u01c9\u01cb\t\f\2\2\u01ca\u01cc\t\r\2\2\u01cb")
        buf.write("\u01ca\3\2\2\2\u01cb\u01cc\3\2\2\2\u01cc\u01ce\3\2\2\2")
        buf.write("\u01cd\u01cf\t\5\2\2\u01ce\u01cd\3\2\2\2\u01cf\u01d0\3")
        buf.write("\2\2\2\u01d0\u01ce\3\2\2\2\u01d0\u01d1\3\2\2\2\u01d1~")
        buf.write("\3\2\2\2\u01d2\u01d6\7$\2\2\u01d3\u01d5\5\u0081A\2\u01d4")
        buf.write("\u01d3\3\2\2\2\u01d5\u01d8\3\2\2\2\u01d6\u01d4\3\2\2\2")
        buf.write("\u01d6\u01d7\3\2\2\2\u01d7\u01d9\3\2\2\2\u01d8\u01d6\3")
        buf.write("\2\2\2\u01d9\u01da\7$\2\2\u01da\u01db\b@\7\2\u01db\u0080")
        buf.write("\3\2\2\2\u01dc\u01e1\n\16\2\2\u01dd\u01de\7)\2\2\u01de")
        buf.write("\u01e1\7$\2\2\u01df\u01e1\5\u0083B\2\u01e0\u01dc\3\2\2")
        buf.write("\2\u01e0\u01dd\3\2\2\2\u01e0\u01df\3\2\2\2\u01e1\u0082")
        buf.write("\3\2\2\2\u01e2\u01e3\7^\2\2\u01e3\u01e4\t\17\2\2\u01e4")
        buf.write("\u0084\3\2\2\2\u01e5\u01e9\t\20\2\2\u01e6\u01e8\t\21\2")
        buf.write("\2\u01e7\u01e6\3\2\2\2\u01e8\u01eb\3\2\2\2\u01e9\u01e7")
        buf.write("\3\2\2\2\u01e9\u01ea\3\2\2\2\u01ea\u0086\3\2\2\2\u01eb")
        buf.write("\u01e9\3\2\2\2\u01ec\u01ee\7&\2\2\u01ed\u01ef\t\21\2\2")
        buf.write("\u01ee\u01ed\3\2\2\2\u01ef\u01f0\3\2\2\2\u01f0\u01ee\3")
        buf.write("\2\2\2\u01f0\u01f1\3\2\2\2\u01f1\u0088\3\2\2\2\u01f2\u01f3")
        buf.write("\7%\2\2\u01f3\u01f4\7%\2\2\u01f4\u01f8\3\2\2\2\u01f5\u01f7")
        buf.write("\13\2\2\2\u01f6\u01f5\3\2\2\2\u01f7\u01fa\3\2\2\2\u01f8")
        buf.write("\u01f9\3\2\2\2\u01f8\u01f6\3\2\2\2\u01f9\u01fb\3\2\2\2")
        buf.write("\u01fa\u01f8\3\2\2\2\u01fb\u01fc\7%\2\2\u01fc\u01fd\7")
        buf.write("%\2\2\u01fd\u01fe\3\2\2\2\u01fe\u01ff\bE\b\2\u01ff\u008a")
        buf.write("\3\2\2\2\u0200\u0202\t\22\2\2\u0201\u0200\3\2\2\2\u0202")
        buf.write("\u0203\3\2\2\2\u0203\u0201\3\2\2\2\u0203\u0204\3\2\2\2")
        buf.write("\u0204\u0205\3\2\2\2\u0205\u0206\bF\b\2\u0206\u008c\3")
        buf.write("\2\2\2\u0207\u0208\13\2\2\2\u0208\u0209\bG\t\2\u0209\u008e")
        buf.write("\3\2\2\2\u020a\u020e\7$\2\2\u020b\u020d\5\u0081A\2\u020c")
        buf.write("\u020b\3\2\2\2\u020d\u0210\3\2\2\2\u020e\u020c\3\2\2\2")
        buf.write("\u020e\u020f\3\2\2\2\u020f\u0212\3\2\2\2\u0210\u020e\3")
        buf.write("\2\2\2\u0211\u0213\t\23\2\2\u0212\u0211\3\2\2\2\u0213")
        buf.write("\u0214\3\2\2\2\u0214\u0215\bH\n\2\u0215\u0090\3\2\2\2")
        buf.write("\u0216\u021a\7$\2\2\u0217\u0219\5\u0081A\2\u0218\u0217")
        buf.write("\3\2\2\2\u0219\u021c\3\2\2\2\u021a\u0218\3\2\2\2\u021a")
        buf.write("\u021b\3\2\2\2\u021b\u0220\3\2\2\2\u021c\u021a\3\2\2\2")
        buf.write("\u021d\u021e\7^\2\2\u021e\u0221\n\17\2\2\u021f\u0221\n")
        buf.write("\24\2\2\u0220\u021d\3\2\2\2\u0220\u021f\3\2\2\2\u0221")
        buf.write("\u0222\3\2\2\2\u0222\u0223\bI\13\2\u0223\u0092\3\2\2\2")
        buf.write("\35\2\u0171\u0175\u017a\u0182\u0187\u0190\u0195\u019e")
        buf.write("\u01a3\u01aa\u01b4\u01ba\u01bf\u01c6\u01cb\u01d0\u01d6")
        buf.write("\u01e0\u01e9\u01f0\u01f8\u0203\u020e\u0212\u021a\u0220")
        buf.write("\f\38\2\39\3\3:\4\3;\5\3<\6\3@\7\b\2\2\3G\b\3H\t\3I\n")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BREAK = 1
    CONTINUE = 2
    IF = 3
    ELSEIF = 4
    ELSE = 5
    FOREACH = 6
    TRUE = 7
    FALSE = 8
    ARRAY = 9
    IN = 10
    INT = 11
    FLOAT = 12
    BOOLEAN = 13
    STRING = 14
    RETURN = 15
    NULL = 16
    CLASS = 17
    VAL = 18
    VAR = 19
    SELF = 20
    CONSTRUCTOR = 21
    DESTRUCTOR = 22
    NEW = 23
    BY = 24
    LB = 25
    RB = 26
    LS = 27
    RS = 28
    DOT = 29
    COMMA = 30
    SEMI = 31
    LP = 32
    RP = 33
    COLON = 34
    ADD = 35
    MINUS = 36
    MUL = 37
    DIV = 38
    MOD = 39
    NOT = 40
    AND = 41
    OR = 42
    EQUAL = 43
    ASSIGN = 44
    DIFF = 45
    GT = 46
    GTE = 47
    LT = 48
    LTE = 49
    STREQ = 50
    STRADD = 51
    DOUBLECOLON = 52
    DOUBLEDOT = 53
    ZERO = 54
    DECINT = 55
    OCTINT = 56
    HEXINT = 57
    BIINT = 58
    FLOATLIT = 59
    STRINGLIT = 60
    ID = 61
    DOLLAR_ID = 62
    COMMENT = 63
    WS = 64
    ERROR_CHAR = 65
    UNCLOSE_STRING = 66
    ILLEGAL_ESCAPE = 67

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Break'", "'Continue'", "'If'", "'Elseif'", "'Else'", "'Foreach'", 
            "'True'", "'False'", "'Array'", "'In'", "'Int'", "'Float'", 
            "'Boolean'", "'String'", "'Return'", "'Null'", "'Class'", "'Val'", 
            "'Var'", "'Self'", "'Constructor'", "'Destructor'", "'New'", 
            "'By'", "'('", "')'", "'['", "']'", "'.'", "','", "';'", "'{'", 
            "'}'", "':'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", 
            "'||'", "'=='", "'='", "'!='", "'>'", "'>='", "'<'", "'<='", 
            "'==.'", "'+.'", "'::'", "'..'" ]

    symbolicNames = [ "<INVALID>",
            "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", "TRUE", 
            "FALSE", "ARRAY", "IN", "INT", "FLOAT", "BOOLEAN", "STRING", 
            "RETURN", "NULL", "CLASS", "VAL", "VAR", "SELF", "CONSTRUCTOR", 
            "DESTRUCTOR", "NEW", "BY", "LB", "RB", "LS", "RS", "DOT", "COMMA", 
            "SEMI", "LP", "RP", "COLON", "ADD", "MINUS", "MUL", "DIV", "MOD", 
            "NOT", "AND", "OR", "EQUAL", "ASSIGN", "DIFF", "GT", "GTE", 
            "LT", "LTE", "STREQ", "STRADD", "DOUBLECOLON", "DOUBLEDOT", 
            "ZERO", "DECINT", "OCTINT", "HEXINT", "BIINT", "FLOATLIT", "STRINGLIT", 
            "ID", "DOLLAR_ID", "COMMENT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", 
                  "TRUE", "FALSE", "ARRAY", "IN", "INT", "FLOAT", "BOOLEAN", 
                  "STRING", "RETURN", "NULL", "CLASS", "VAL", "VAR", "SELF", 
                  "CONSTRUCTOR", "DESTRUCTOR", "NEW", "BY", "LB", "RB", 
                  "LS", "RS", "DOT", "COMMA", "SEMI", "LP", "RP", "COLON", 
                  "ADD", "MINUS", "MUL", "DIV", "MOD", "NOT", "AND", "OR", 
                  "EQUAL", "ASSIGN", "DIFF", "GT", "GTE", "LT", "LTE", "STREQ", 
                  "STRADD", "DOUBLECOLON", "DOUBLEDOT", "ZERO", "DECINT", 
                  "OCTINT", "HEXINT", "BIINT", "FLOATLIT", "INTFLOAT", "DECFLOAT", 
                  "EXPFLOAT", "STRINGLIT", "STRINGBODY", "STRING_ESCAPE", 
                  "ID", "DOLLAR_ID", "COMMENT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

    grammarFileName = "D96.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:
            raise UncloseString(result.text[1:])
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text[1:])
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        else:
            return result;


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[54] = self.DECINT_action 
            actions[55] = self.OCTINT_action 
            actions[56] = self.HEXINT_action 
            actions[57] = self.BIINT_action 
            actions[58] = self.FLOATLIT_action 
            actions[62] = self.STRINGLIT_action 
            actions[69] = self.ERROR_CHAR_action 
            actions[70] = self.UNCLOSE_STRING_action 
            actions[71] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def DECINT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            y = str(self.text)
            x = y.replace("_", "")
            self.text = x[0:]

     

    def OCTINT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            y = str(self.text)
            x = y.replace("_", "")
            self.text = x[0:]

     

    def HEXINT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            y = str(self.text)
            x = y.replace("_", "")
            self.text = x[0:]

     

    def BIINT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            y = str(self.text)
            x = y.replace("_", "")
            self.text = x[0:]

     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            y = str(self.text)
            x = y.replace("_", "")
            self.text = x[0:]

     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

            y = str(self.text)
            self.text = y[1:-1]

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 7:

            y = str(self.text)
            error = ['\b', '\t', '\n', '\f', '\r' , '"', "'", '\\']
            if y[-1] in error:
            	raise UncloseString(y[1:-1])
            else:
                raise UncloseString(y[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 8:

            y = str(self.text)
            raise IllegalEscape(y[1:])

     


