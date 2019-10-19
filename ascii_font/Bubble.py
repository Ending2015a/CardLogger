

if not '.' in __name__:
    package_name = '__main__'
else:
    package_name = __name__.rsplit(".", 1)[0]

if package_name == "__main__":
    module_name = 'base'
else:
    module_name = package_name + '.' + 'base'

module = __import__(module_name, fromlist=['.'])
AsciiFont = getattr(module, 'AsciiFont')


Bubble = AsciiFont("")
# flf2a 4 3 8 15 11 0 10127 242


# Bubble by Glenn Chappell 4/93
# Includes characters 128-255
# Enhanced for Latin-2,3,4 by John Cowan <cowan@ccil.org>
# Latin character sets supported only if your screen font does
# figlet release 2.2 -- November 1996
# Permission is hereby given to modify this font, as long as the
# modifier's name is placed on a comment line.
# Modified by Paul Burton <solution@earthlink.net> 12/96 to include new parameter
# supported by FIGlet and FIGWin.  May also be slightly modified for better use
# of new full-width/kern/smush alternatives, but default output is NOT changed.
Bubble[" "] = (
" \n"
" \n"
" \n"
" "
)

Bubble["!"] = (
"   _  \n"
"  / \\ \n"
" ( ! )\n"
"  \\_/ "
)

Bubble["\""] = (
"   _  \n"
"  / \\ \n"
" ( \" )\n"
"  \\_/ "
)

Bubble["#"] = (
"   _  \n"
"  / \\ \n"
" ( \n )\n"
"  \\_/ "
)

Bubble["$"] = (
"   _  \n"
"  / \\ \n"
" ( $ )\n"
"  \\_/ "
)

Bubble["%"] = (
"   _  \n"
"  / \\ \n"
" ( % )\n"
"  \\_/ "
)

Bubble["&"] = (
"   _  \n"
"  / \\ \n"
" ( & )\n"
"  \\_/ "
)

Bubble["'"] = (
"   _  \n"
"  / \\ \n"
" ( ' )\n"
"  \\_/ "
)

Bubble["("] = (
"   _  \n"
"  / \\ \n"
" ( ( )\n"
"  \\_/ "
)

Bubble[")"] = (
"   _  \n"
"  / \\ \n"
" ( ) )\n"
"  \\_/ "
)

Bubble["*"] = (
"   _  \n"
"  / \\ \n"
" ( * )\n"
"  \\_/ "
)

Bubble["+"] = (
"   _  \n"
"  / \\ \n"
" ( + )\n"
"  \\_/ "
)

Bubble[","] = (
"   _  \n"
"  / \\ \n"
" ( , )\n"
"  \\_/ "
)

Bubble["-"] = (
"   _  \n"
"  / \\ \n"
" ( - )\n"
"  \\_/ "
)

Bubble["."] = (
"   _  \n"
"  / \\ \n"
" ( . )\n"
"  \\_/ "
)

Bubble["/"] = (
"   _  \n"
"  / \\ \n"
" ( / )\n"
"  \\_/ "
)

Bubble["0"] = (
"   _  \n"
"  / \\ \n"
" ( 0 )\n"
"  \\_/ "
)

Bubble["1"] = (
"   _  \n"
"  / \\ \n"
" ( 1 )\n"
"  \\_/ "
)

Bubble["2"] = (
"   _  \n"
"  / \\ \n"
" ( 2 )\n"
"  \\_/ "
)

Bubble["3"] = (
"   _  \n"
"  / \\ \n"
" ( 3 )\n"
"  \\_/ "
)

Bubble["4"] = (
"   _  \n"
"  / \\ \n"
" ( 4 )\n"
"  \\_/ "
)

Bubble["5"] = (
"   _  \n"
"  / \\ \n"
" ( 5 )\n"
"  \\_/ "
)

Bubble["6"] = (
"   _  \n"
"  / \\ \n"
" ( 6 )\n"
"  \\_/ "
)

Bubble["7"] = (
"   _  \n"
"  / \\ \n"
" ( 7 )\n"
"  \\_/ "
)

Bubble["8"] = (
"   _  \n"
"  / \\ \n"
" ( 8 )\n"
"  \\_/ "
)

Bubble["9"] = (
"   _  \n"
"  / \\ \n"
" ( 9 )\n"
"  \\_/ "
)

Bubble[":"] = (
"   _  \n"
"  / \\ \n"
" ( : )\n"
"  \\_/ "
)

Bubble[";"] = (
"   _  \n"
"  / \\ \n"
" ( ; )\n"
"  \\_/ "
)

Bubble["<"] = (
"   _  \n"
"  / \\ \n"
" ( < )\n"
"  \\_/ "
)

Bubble["="] = (
"   _  \n"
"  / \\ \n"
" ( = )\n"
"  \\_/ "
)

Bubble[">"] = (
"   _  \n"
"  / \\ \n"
" ( > )\n"
"  \\_/ "
)

Bubble["?"] = (
"   _  \n"
"  / \\ \n"
" ( ? )\n"
"  \\_/ "
)

Bubble["@"] = (
"   _  \n"
"  / \\ \n"
" ( \n )\n"
"  \\_/ "
)

Bubble["A"] = (
"   _  \n"
"  / \\ \n"
" ( A )\n"
"  \\_/ "
)

Bubble["B"] = (
"   _  \n"
"  / \\ \n"
" ( B )\n"
"  \\_/ "
)

Bubble["C"] = (
"   _  \n"
"  / \\ \n"
" ( C )\n"
"  \\_/ "
)

Bubble["D"] = (
"   _  \n"
"  / \\ \n"
" ( D )\n"
"  \\_/ "
)

Bubble["E"] = (
"   _  \n"
"  / \\ \n"
" ( E )\n"
"  \\_/ "
)

Bubble["F"] = (
"   _  \n"
"  / \\ \n"
" ( F )\n"
"  \\_/ "
)

Bubble["G"] = (
"   _  \n"
"  / \\ \n"
" ( G )\n"
"  \\_/ "
)

Bubble["H"] = (
"   _  \n"
"  / \\ \n"
" ( H )\n"
"  \\_/ "
)

Bubble["I"] = (
"   _  \n"
"  / \\ \n"
" ( I )\n"
"  \\_/ "
)

Bubble["J"] = (
"   _  \n"
"  / \\ \n"
" ( J )\n"
"  \\_/ "
)

Bubble["K"] = (
"   _  \n"
"  / \\ \n"
" ( K )\n"
"  \\_/ "
)

Bubble["L"] = (
"   _  \n"
"  / \\ \n"
" ( L )\n"
"  \\_/ "
)

Bubble["M"] = (
"   _  \n"
"  / \\ \n"
" ( M )\n"
"  \\_/ "
)

Bubble["N"] = (
"   _  \n"
"  / \\ \n"
" ( N )\n"
"  \\_/ "
)

Bubble["O"] = (
"   _  \n"
"  / \\ \n"
" ( O )\n"
"  \\_/ "
)

Bubble["P"] = (
"   _  \n"
"  / \\ \n"
" ( P )\n"
"  \\_/ "
)

Bubble["Q"] = (
"   _  \n"
"  / \\ \n"
" ( Q )\n"
"  \\_/ "
)

Bubble["R"] = (
"   _  \n"
"  / \\ \n"
" ( R )\n"
"  \\_/ "
)

Bubble["S"] = (
"   _  \n"
"  / \\ \n"
" ( S )\n"
"  \\_/ "
)

Bubble["T"] = (
"   _  \n"
"  / \\ \n"
" ( T )\n"
"  \\_/ "
)

Bubble["U"] = (
"   _  \n"
"  / \\ \n"
" ( U )\n"
"  \\_/ "
)

Bubble["V"] = (
"   _  \n"
"  / \\ \n"
" ( V )\n"
"  \\_/ "
)

Bubble["W"] = (
"   _  \n"
"  / \\ \n"
" ( W )\n"
"  \\_/ "
)

Bubble["X"] = (
"   _  \n"
"  / \\ \n"
" ( X )\n"
"  \\_/ "
)

Bubble["Y"] = (
"   _  \n"
"  / \\ \n"
" ( Y )\n"
"  \\_/ "
)

Bubble["Z"] = (
"   _  \n"
"  / \\ \n"
" ( Z )\n"
"  \\_/ "
)

Bubble["["] = (
"   _  \n"
"  / \\ \n"
" ( [ )\n"
"  \\_/ "
)

Bubble["\\"] = (
"   _  \n"
"  / \\ \n"
" ( \\ )\n"
"  \\_/ "
)

Bubble["]"] = (
"   _  \n"
"  / \\ \n"
" ( ] )\n"
"  \\_/ "
)

Bubble["^"] = (
"   _  \n"
"  / \\ \n"
" ( ^ )\n"
"  \\_/ "
)

Bubble["_"] = (
"   _  \n"
"  / \\ \n"
" ( _ )\n"
"  \\_/ "
)

Bubble["`"] = (
"   _  \n"
"  / \\ \n"
" ( ` )\n"
"  \\_/ "
)

Bubble["a"] = (
"   _  \n"
"  / \\ \n"
" ( a )\n"
"  \\_/ "
)

Bubble["b"] = (
"   _  \n"
"  / \\ \n"
" ( b )\n"
"  \\_/ "
)

Bubble["c"] = (
"   _  \n"
"  / \\ \n"
" ( c )\n"
"  \\_/ "
)

Bubble["d"] = (
"   _  \n"
"  / \\ \n"
" ( d )\n"
"  \\_/ "
)

Bubble["e"] = (
"   _  \n"
"  / \\ \n"
" ( e )\n"
"  \\_/ "
)

Bubble["f"] = (
"   _  \n"
"  / \\ \n"
" ( f )\n"
"  \\_/ "
)

Bubble["g"] = (
"   _  \n"
"  / \\ \n"
" ( g )\n"
"  \\_/ "
)

Bubble["h"] = (
"   _  \n"
"  / \\ \n"
" ( h )\n"
"  \\_/ "
)

Bubble["i"] = (
"   _  \n"
"  / \\ \n"
" ( i )\n"
"  \\_/ "
)

Bubble["j"] = (
"   _  \n"
"  / \\ \n"
" ( j )\n"
"  \\_/ "
)

Bubble["k"] = (
"   _  \n"
"  / \\ \n"
" ( k )\n"
"  \\_/ "
)

Bubble["l"] = (
"   _  \n"
"  / \\ \n"
" ( l )\n"
"  \\_/ "
)

Bubble["m"] = (
"   _  \n"
"  / \\ \n"
" ( m )\n"
"  \\_/ "
)

Bubble["n"] = (
"   _  \n"
"  / \\ \n"
" ( n )\n"
"  \\_/ "
)

Bubble["o"] = (
"   _  \n"
"  / \\ \n"
" ( o )\n"
"  \\_/ "
)

Bubble["p"] = (
"   _  \n"
"  / \\ \n"
" ( p )\n"
"  \\_/ "
)

Bubble["q"] = (
"   _  \n"
"  / \\ \n"
" ( q )\n"
"  \\_/ "
)

Bubble["r"] = (
"   _  \n"
"  / \\ \n"
" ( r )\n"
"  \\_/ "
)

Bubble["s"] = (
"   _  \n"
"  / \\ \n"
" ( s )\n"
"  \\_/ "
)

Bubble["t"] = (
"   _  \n"
"  / \\ \n"
" ( t )\n"
"  \\_/ "
)

Bubble["u"] = (
"   _  \n"
"  / \\ \n"
" ( u )\n"
"  \\_/ "
)

Bubble["v"] = (
"   _  \n"
"  / \\ \n"
" ( v )\n"
"  \\_/ "
)

Bubble["w"] = (
"   _  \n"
"  / \\ \n"
" ( w )\n"
"  \\_/ "
)

Bubble["x"] = (
"   _  \n"
"  / \\ \n"
" ( x )\n"
"  \\_/ "
)

Bubble["y"] = (
"   _  \n"
"  / \\ \n"
" ( y )\n"
"  \\_/ "
)

Bubble["z"] = (
"   _  \n"
"  / \\ \n"
" ( z )\n"
"  \\_/ "
)

Bubble["{"] = (
"   _  \n"
"  / \\ \n"
" ( { )\n"
"  \\_/ "
)

Bubble["|"] = (
"   _  \n"
"  / \\ \n"
" ( | )\n"
"  \\_/ "
)

Bubble["}"] = (
"   _  \n"
"  / \\ \n"
" ( } )\n"
"  \\_/ "
)

Bubble["~"] = (
"   _  \n"
"  / \\ \n"
" ( ~ )\n"
"  \\_/ "
)

