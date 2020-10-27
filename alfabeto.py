# Palavras reservadas
ARRAY = 0
BOOLEAN = 1
BREAK = 2
CHAR = 3
CONTINUE = 4
DO = 5
ELSE = 6
FALSE = 7
FUNCTION = 8
IF = 9
INTEGER = 10
OF = 11
STRING = 12
STRUCT = 13 
TRUE = 14
TYPE = 15
VAR = 16
WHILE = 17
# Simbolos
COLON = 18
SEMI_COLON = 19
COMMA = 20
EQUALS = 21
LEFT_SQUARE = 22
RIGHT_SQUARE = 23
LEFT_BRACES = 24
RIGHT_BRACES = 25
LEFT_PARENTHESIS = 26
RIGHT_PARENTHESIS = 27
AND = 28
OR = 29
LESS_THAN = 30
GREATER_THAN = 31
LESS_OR_EQUAL = 32
GREATER_OR_EQUAL = 33
NOT_EQUAL = 34
EQUAL_EQUAL = 35
PLUS = 36
PLUS_PLUS = 37
MINUS = 38
MINUS_MINUS = 39
TIMES = 40
DIVIDE = 41
DOT = 42
NOT = 43
# Tokens regulares
CHARACTER = 44
NUMERAL = 45
STRINGVAL = 46
ID = 47
# Token desconhecido
UNKNOWN = 48
# Fim do arquivo
EOF=49

palavras_reservadas = ["array", "boolean", "break", "char", "continue", "do", "else", "false", "function", "if", "integer", "of", "string", "struct", "true", "type", "var", "while"]
simbolos = ["colon","semi_colon","comma","equals","left_square","right_square","left_braces",
            "right_braces","left_parenthesis","right_parenthesis","and","or",
            "less_than","greater_than","less_or_equal","greater_or_equal","not_equal",
            "equal_equal","plus","plus_plus","minus","minus_minus","times","divide","dot","not"]
tokens_regulares = ["character", "numeral", "stringval", "id"]