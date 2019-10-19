

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


Buldhead = AsciiFont("$")
# flf2a$ 4 4 99 0 20


# Bulbhead by Jef Poskanzer, 23jun94
# Figlet release 2.0 -- August 5, 1993
#  ____  __  __  __    ____  _   _  ____    __    ____
# (  _ \(  )(  )(  )  (  _ \( )_( )( ___)  /__\  (  _ \
#  ) _ < )(__)(  )(__  ) _ < ) _ (  )___) /(__)\  )(_) )
# (____/(______)(____)(____/(_) (_)(____)(__)(__)(____/
# Update February 12, 2002 by Markus Gebhard markus@jave.de
#   Added german umlauts
# Explanation of first line:
# flf2 - "magic number" for file identification
# a    - should always be `a', for now
# $    - the "hardblank" -- prints as a blank, but can't be smushed
# 4    - height of a character
# 4    - height of a character, not including descenders
# 99   - max line length (excluding comment lines) + a fudge factor
# 0    - default smushmode for this font (like "-m 0" on command line)
# 13   - number of comment lines
Buldhead[" "] = (
"$$\n"
"$$\n"
"$$\n"
"$$"
)

Buldhead["!"] = (
"/\\\n"
")(\n"
"\\/\n"
"()"
)

Buldhead["\""] = (
"||\n"
"  \n"
"  \n"
"  "
)

Buldhead["#"] = (
" | | \n"
"-|-|-\n"
"-|-|-\n"
" | | "
)

Buldhead["$"] = (
" _|_ \n"
"/ |_)\n"
"\\_| \\\n"
"(_|_/"
)

Buldhead["%"] = (
" _  _  \n"
"(_)/ ) \n"
"  / /_ \n"
" (_/(_)"
)

Buldhead["&"] = (
"  _  \n"
" ( ) \n"
" /_\\/\n"
"(__/\\"
)

Buldhead["'"] = (
"/\n"
" \n"
" \n"
" "
)

Buldhead["("] = (
"  _ \n"
" / )\n"
"( ( \n"
" \\_)"
)

Buldhead[")"] = (
" _  \n"
"( \\ \n"
" ) )\n"
"(_/ "
)

Buldhead["*"] = (
"   \n"
"\\|/\n"
"/|\\\n"
"   "
)

Buldhead["+"] = (
"   _   \n"
" _| |_ \n"
"(_   _)\n"
"  |_|  "
)

Buldhead[","] = (
"  \n"
"  \n"
"()\n"
"/ "
)

Buldhead["-"] = (
"     \n"
" ___ \n"
"(___)\n"
"     "
)

Buldhead["."] = (
"  \n"
"  \n"
"  \n"
"()"
)

Buldhead["/"] = (
"   _ \n"
"  / )\n"
" / / \n"
"(_/  "
)

Buldhead["0"] = (
"  ___  \n"
" / _ \\ \n"
"( (_) )\n"
" \\___/ "
)

Buldhead["1"] = (
"  __ \n"
" /  )\n"
"  )( \n"
" (__)"
)

Buldhead["2"] = (
" ___  \n"
"(__ \\ \n"
" / _/ \n"
"(____)"
)

Buldhead["3"] = (
" ___ \n"
"(__ )\n"
" (_ \\\n"
"(___/"
)

Buldhead["4"] = (
"  __  \n"
" /. | \n"
"(_  _)\n"
"  (_) "
)

Buldhead["5"] = (
" ___ \n"
"| __)\n"
"|__ \\\n"
"(___/"
)

Buldhead["6"] = (
"  _  \n"
" / ) \n"
"/ _ \\\n"
"\\___/"
)

Buldhead["7"] = (
" ___ \n"
"(__ )\n"
" / / \n"
"(_/  "
)

Buldhead["8"] = (
" ___ \n"
"( _ )\n"
"/ _ \\\n"
"\\___/"
)

Buldhead["9"] = (
" ___ \n"
"/ _ \\\n"
"\\_  /\n"
" (_/ "
)

Buldhead[":"] = (
"  \n"
"()\n"
"  \n"
"()"
)

Buldhead[";"] = (
"()\n"
"  \n"
"()\n"
"/ "
)

Buldhead["<"] = (
"  __\n"
" / /\n"
"< < \n"
" \\_\\"
)

Buldhead["="] = (
" ___ \n"
"(___)\n"
" ___ \n"
"(___)"
)

Buldhead[">"] = (
"__  \n"
"\\ \\ \n"
" > >\n"
"/_/ "
)

Buldhead["?"] = (
" ___ \n"
"(__ )\n"
" (_/ \n"
" (_) "
)

Buldhead["@"] = (
"  __ \n"
" /  \\\n"
"| ()/\n"
" \\__ "
)

Buldhead["A"] = (
"   __   \n"
"  /__\\  \n"
" /(__)\\ \n"
"(__)(__)"
)

Buldhead["B"] = (
" ____ \n"
"(  _ \\\n"
" ) _ <\n"
"(____/"
)

Buldhead["C"] = (
"  ___ \n"
" / __)\n"
"( (__ \n"
" \\___)"
)

Buldhead["D"] = (
" ____  \n"
"(  _ \\ \n"
" )(_) )\n"
"(____/ "
)

Buldhead["E"] = (
" ____ \n"
"( ___)\n"
" )__) \n"
"(____)"
)

Buldhead["F"] = (
" ____ \n"
"( ___)\n"
" )__) \n"
"(__)  "
)

Buldhead["G"] = (
"  ___ \n"
" / __)\n"
"( (_-.\n"
" \\___/"
)

Buldhead["H"] = (
" _   _ \n"
"( )_( )\n"
" ) _ ( \n"
"(_) (_)"
)

Buldhead["I"] = (
" ____ \n"
"(_  _)\n"
" _)(_ \n"
"(____)"
)

Buldhead["J"] = (
"  ____ \n"
" (_  _)\n"
".-_)(  \n"
"\\____) "
)

Buldhead["K"] = (
" _  _ \n"
"( )/ )\n"
" )  ( \n"
"(_)\\_)"
)

Buldhead["L"] = (
" __   \n"
"(  )  \n"
" )(__ \n"
"(____)"
)

Buldhead["M"] = (
" __  __ \n"
"(  \\/  )\n"
" )    ( \n"
"(_/\\/\\_)"
)

Buldhead["N"] = (
" _  _ \n"
"( \\( )\n"
" )  ( \n"
"(_)\\_)"
)

Buldhead["O"] = (
" _____ \n"
"(  _  )\n"
" )(_)( \n"
"(_____)"
)

Buldhead["P"] = (
" ____ \n"
"(  _ \\\n"
" )___/\n"
"(__)  "
)

Buldhead["Q"] = (
" _____ \n"
"(  _  )\n"
" )(_)( \n"
"(___/\\\\"
)

Buldhead["R"] = (
" ____ \n"
"(  _ \\\n"
" )   /\n"
"(_)\\_)"
)

Buldhead["S"] = (
" ___ \n"
"/ __)\n"
"\\__ \\\n"
"(___/"
)

Buldhead["T"] = (
" ____ \n"
"(_  _)\n"
"  )(  \n"
" (__) "
)

Buldhead["U"] = (
" __  __ \n"
"(  )(  )\n"
" )(__)( \n"
"(______)"
)

Buldhead["V"] = (
" _  _ \n"
"( \\/ )\n"
" \\  / \n"
"  \\/  "
)

Buldhead["W"] = (
" _    _ \n"
"( \\/\\/ )\n"
" )    ( \n"
"(__/\\__)"
)

Buldhead["X"] = (
" _  _ \n"
"( \\/ )\n"
" )  ( \n"
"(_/\\_)"
)

Buldhead["Y"] = (
" _  _ \n"
"( \\/ )\n"
" \\  / \n"
" (__) "
)

Buldhead["Z"] = (
" ____ \n"
"(_   )\n"
" / /_ \n"
"(____)"
)

Buldhead["["] = (
" __\n"
"|  \n"
"|  \n"
"|__"
)

Buldhead["\\"] = (
" _   \n"
"( \\  \n"
" \\ \\ \n"
"  \\_)"
)

Buldhead["]"] = (
"__ \n"
"  |\n"
"  |\n"
"__|"
)

Buldhead["^"] = (
" / \\ \n"
"(_^_)\n"
"     \n"
"     "
)

Buldhead["_"] = (
"     \n"
"     \n"
" ___ \n"
"(___)"
)

Buldhead["`"] = (
"\\\n"
" \n"
" \n"
" "
)

Buldhead["a"] = (
"   __   \n"
"  /__\\  \n"
" /(__)\\ \n"
"(__)(__)"
)

Buldhead["b"] = (
" ____ \n"
"(  _ \\\n"
" ) _ <\n"
"(____/"
)

Buldhead["c"] = (
"  ___ \n"
" / __)\n"
"( (__ \n"
" \\___)"
)

Buldhead["d"] = (
" ____  \n"
"(  _ \\ \n"
" )(_) )\n"
"(____/ "
)

Buldhead["e"] = (
" ____ \n"
"( ___)\n"
" )__) \n"
"(____)"
)

Buldhead["f"] = (
" ____ \n"
"( ___)\n"
" )__) \n"
"(__)  "
)

Buldhead["g"] = (
"  ___ \n"
" / __)\n"
"( (_-.\n"
" \\___/"
)

Buldhead["h"] = (
" _   _ \n"
"( )_( )\n"
" ) _ ( \n"
"(_) (_)"
)

Buldhead["i"] = (
" ____ \n"
"(_  _)\n"
" _)(_ \n"
"(____)"
)

Buldhead["j"] = (
"  ____ \n"
" (_  _)\n"
".-_)(  \n"
"\\____) "
)

Buldhead["k"] = (
" _  _ \n"
"( )/ )\n"
" )  ( \n"
"(_)\\_)"
)

Buldhead["l"] = (
" __   \n"
"(  )  \n"
" )(__ \n"
"(____)"
)

Buldhead["m"] = (
" __  __ \n"
"(  \\/  )\n"
" )    ( \n"
"(_/\\/\\_)"
)

Buldhead["n"] = (
" _  _ \n"
"( \\( )\n"
" )  ( \n"
"(_)\\_)"
)

Buldhead["o"] = (
" _____ \n"
"(  _  )\n"
" )(_)( \n"
"(_____)"
)

Buldhead["p"] = (
" ____ \n"
"(  _ \\\n"
" )___/\n"
"(__)  "
)

Buldhead["q"] = (
" _____ \n"
"(  _  )\n"
" )(_)( \n"
"(___/\\\\"
)

Buldhead["r"] = (
" ____ \n"
"(  _ \\\n"
" )   /\n"
"(_)\\_)"
)

Buldhead["s"] = (
" ___ \n"
"/ __)\n"
"\\__ \\\n"
"(___/"
)

Buldhead["t"] = (
" ____ \n"
"(_  _)\n"
"  )(  \n"
" (__) "
)

Buldhead["u"] = (
" __  __ \n"
"(  )(  )\n"
" )(__)( \n"
"(______)"
)

Buldhead["v"] = (
" _  _ \n"
"( \\/ )\n"
" \\  / \n"
"  \\/  "
)

Buldhead["w"] = (
" _    _ \n"
"( \\/\\/ )\n"
" )    ( \n"
"(__/\\__)"
)

Buldhead["x"] = (
" _  _ \n"
"( \\/ )\n"
" )  ( \n"
"(_/\\_)"
)

Buldhead["y"] = (
" _  _ \n"
"( \\/ )\n"
" \\  / \n"
" (__) "
)

Buldhead["z"] = (
" ____ \n"
"(_   )\n"
" / /_ \n"
"(____)"
)

Buldhead["{"] = (
" ,-\n"
"_| \n"
" | \n"
" `-"
)

Buldhead["|"] = (
"/\\\n"
"||\n"
"||\n"
"\\/"
)

Buldhead["}"] = (
"-. \n"
" |_\n"
" | \n"
"-' "
)

Buldhead["~"] = (
"   \n"
"/\\/\n"
"   \n"
"   "
)

