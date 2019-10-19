

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


Slant = AsciiFont("$")
# flf2a$ 6 5 16 15 10 0 18319


# Slant by Glenn Chappell 3/93 -- based on Standard
# Includes ISO Latin-1
# figlet release 2.1 -- 12 Aug 1994
# Permission is hereby given to modify this font, as long as the
# modifier's name is placed on a comment line.
# Modified by Paul Burton <solution@earthlink.net> 12/96 to include new parameter
# supported by FIGlet and FIGWin.  May also be slightly modified for better use
# of new full-width/kern/smush alternatives, but default output is NOT changed.
Slant[" "] = (
"     $$\n"
"    $$ \n"
"   $$  \n"
"  $$   \n"
" $$    \n"
"$$     "
)

Slant["!"] = (
"    __\n"
"   / /\n"
"  / / \n"
" /_/  \n"
"(_)   \n"
"      "
)

Slant["\""] = (
" _ _ \n"
"( | )\n"
"|/|/ \n"
" $   \n"
"$    \n"
"     "
)

Slant["#"] = (
"     __ __ \n"
"  __/ // /_\n"
" /_  _  __/\n"
"/_  _  __/ \n"
" /_//_/    \n"
"           "
)

Slant["$"] = (
"     __\n"
"   _/ /\n"
"  / __/\n"
" (_  ) \n"
"/  _/  \n"
"/_/    "
)

Slant["%"] = (
"   _   __\n"
"  (_)_/_/\n"
"   _/_/  \n"
" _/_/_   \n"
"/_/ (_)  \n"
"         "
)

Slant["&"] = (
"   ___   \n"
"  ( _ )  \n"
" / __ \\/|\n"
"/ /_/  < \n"
"\\____/\\/ \n"
"         "
)

Slant["'"] = (
"  _ \n"
" ( )\n"
" |/ \n"
" $  \n"
"$   \n"
"    "
)

Slant["("] = (
"     __\n"
"   _/_/\n"
"  / /  \n"
" / /   \n"
"/ /    \n"
"|_|    "
)

Slant[")"] = (
"     _ \n"
"    | |\n"
"    / /\n"
"   / / \n"
" _/_/  \n"
"/_/    "
)

Slant["*"] = (
"       \n"
"  __/|_\n"
" |    /\n"
"/_ __| \n"
" |/    \n"
"       "
)

Slant["+"] = (
"       \n"
"    __ \n"
" __/ /_\n"
"/_  __/\n"
" /_/   \n"
"       "
)

Slant[","] = (
"   \n"
"   \n"
"   \n"
" _ \n"
"( )\n"
"|/ "
)

Slant["-"] = (
"       \n"
"       \n"
" ______\n"
"/_____/\n"
"  $    \n"
"       "
)

Slant["."] = (
"   \n"
"   \n"
"   \n"
" _ \n"
"(_)\n"
"   "
)

Slant["/"] = (
"       __\n"
"     _/_/\n"
"   _/_/  \n"
" _/_/    \n"
"/_/      \n"
"         "
)

Slant["0"] = (
"   ____ \n"
"  / __ \\\n"
" / / / /\n"
"/ /_/ / \n"
"\\____/  \n"
"        "
)

Slant["1"] = (
"   ___\n"
"  <  /\n"
"  / / \n"
" / /  \n"
"/_/   \n"
"      "
)

Slant["2"] = (
"   ___ \n"
"  |__ \\\n"
"  __/ /\n"
" / __/ \n"
"/____/ \n"
"       "
)

Slant["3"] = (
"   _____\n"
"  |__  /\n"
"   /_ < \n"
" ___/ / \n"
"/____/  \n"
"        "
)

Slant["4"] = (
"   __ __\n"
"  / // /\n"
" / // /_\n"
"/__  __/\n"
"  /_/   \n"
"        "
)

Slant["5"] = (
"    ______\n"
"   / ____/\n"
"  /___ \\  \n"
" ____/ /  \n"
"/_____/   \n"
"          "
)

Slant["6"] = (
"   _____\n"
"  / ___/\n"
" / __ \\ \n"
"/ /_/ / \n"
"\\____/  \n"
"        "
)

Slant["7"] = (
" _____\n"
"/__  /\n"
"  / / \n"
" / /  \n"
"/_/   \n"
"      "
)

Slant["8"] = (
"   ____ \n"
"  ( __ )\n"
" / __  |\n"
"/ /_/ / \n"
"\\____/  \n"
"        "
)

Slant["9"] = (
"   ____ \n"
"  / __ \\\n"
" / /_/ /\n"
" \\__, / \n"
"/____/  \n"
"        "
)

Slant[":"] = (
"     \n"
"   _ \n"
"  (_)\n"
" _   \n"
"(_)  \n"
"     "
)

Slant[";"] = (
"     \n"
"   _ \n"
"  (_)\n"
" _   \n"
"( )  \n"
"|/   "
)

Slant["<"] = (
"  __\n"
" / /\n"
"/ / \n"
"\\ \\ \n"
" \\_\\\n"
"    "
)

Slant["="] = (
"       \n"
"  _____\n"
" /____/\n"
"/____/ \n"
"  $    \n"
"       "
)

Slant[">"] = (
"__  \n"
"\\ \\ \n"
" \\ \\\n"
" / /\n"
"/_/ \n"
"    "
)

Slant["?"] = (
"  ___ \n"
" /__ \\\n"
"  / _/\n"
" /_/  \n"
"(_)   \n"
"      "
)

Slant["@"] = (
"   ______ \n"
"  / ____ \\\n"
" / / __ `/\n"
"/ / /_/ / \n"
"\\ \\__,_/  \n"
" \\____/   "
)

Slant["A"] = (
"    ___ \n"
"   /   |\n"
"  / /| |\n"
" / ___ |\n"
"/_/  |_|\n"
"        "
)

Slant["B"] = (
"    ____ \n"
"   / __ )\n"
"  / __  |\n"
" / /_/ / \n"
"/_____/  \n"
"         "
)

Slant["C"] = (
"   ______\n"
"  / ____/\n"
" / /     \n"
"/ /___   \n"
"\\____/   \n"
"         "
)

Slant["D"] = (
"    ____ \n"
"   / __ \\\n"
"  / / / /\n"
" / /_/ / \n"
"/_____/  \n"
"         "
)

Slant["E"] = (
"    ______\n"
"   / ____/\n"
"  / __/   \n"
" / /___   \n"
"/_____/   \n"
"          "
)

Slant["F"] = (
"    ______\n"
"   / ____/\n"
"  / /_    \n"
" / __/    \n"
"/_/       \n"
"          "
)

Slant["G"] = (
"   ______\n"
"  / ____/\n"
" / / __  \n"
"/ /_/ /  \n"
"\\____/   \n"
"         "
)

Slant["H"] = (
"    __  __\n"
"   / / / /\n"
"  / /_/ / \n"
" / __  /  \n"
"/_/ /_/   \n"
"          "
)

Slant["I"] = (
"    ____\n"
"   /  _/\n"
"   / /  \n"
" _/ /   \n"
"/___/   \n"
"        "
)

Slant["J"] = (
"       __\n"
"      / /\n"
" __  / / \n"
"/ /_/ /  \n"
"\\____/   \n"
"         "
)

Slant["K"] = (
"    __ __\n"
"   / //_/\n"
"  / ,<   \n"
" / /| |  \n"
"/_/ |_|  \n"
"         "
)

Slant["L"] = (
"    __ \n"
"   / / \n"
"  / /  \n"
" / /___\n"
"/_____/\n"
"       "
)

Slant["M"] = (
"    __  ___\n"
"   /  |/  /\n"
"  / /|_/ / \n"
" / /  / /  \n"
"/_/  /_/   \n"
"           "
)

Slant["N"] = (
"    _   __\n"
"   / | / /\n"
"  /  |/ / \n"
" / /|  /  \n"
"/_/ |_/   \n"
"          "
)

Slant["O"] = (
"   ____ \n"
"  / __ \\\n"
" / / / /\n"
"/ /_/ / \n"
"\\____/  \n"
"        "
)

Slant["P"] = (
"    ____ \n"
"   / __ \\\n"
"  / /_/ /\n"
" / ____/ \n"
"/_/      \n"
"         "
)

Slant["Q"] = (
"   ____ \n"
"  / __ \\\n"
" / / / /\n"
"/ /_/ / \n"
"\\___\\_\\ \n"
"        "
)

Slant["R"] = (
"    ____ \n"
"   / __ \\\n"
"  / /_/ /\n"
" / _, _/ \n"
"/_/ |_|  \n"
"         "
)

Slant["S"] = (
"   _____\n"
"  / ___/\n"
"  \\__ \\ \n"
" ___/ / \n"
"/____/  \n"
"        "
)

Slant["T"] = (
"  ______\n"
" /_  __/\n"
"  / /   \n"
" / /    \n"
"/_/     \n"
"        "
)

Slant["U"] = (
"   __  __\n"
"  / / / /\n"
" / / / / \n"
"/ /_/ /  \n"
"\\____/   \n"
"         "
)

Slant["V"] = (
" _    __\n"
"| |  / /\n"
"| | / / \n"
"| |/ /  \n"
"|___/   \n"
"        "
)

Slant["W"] = (
" _       __\n"
"| |     / /\n"
"| | /| / / \n"
"| |/ |/ /  \n"
"|__/|__/   \n"
"           "
)

Slant["X"] = (
"   _  __\n"
"  | |/ /\n"
"  |   / \n"
" /   |  \n"
"/_/|_|  \n"
"        "
)

Slant["Y"] = (
"__  __\n"
"\\ \\/ /\n"
" \\  / \n"
" / /  \n"
"/_/   \n"
"      "
)

Slant["Z"] = (
" _____\n"
"/__  /\n"
"  / / \n"
" / /__\n"
"/____/\n"
"      "
)

Slant["["] = (
"     ___\n"
"    / _/\n"
"   / /  \n"
"  / /   \n"
" / /    \n"
"/__/    "
)

Slant["\\"] = (
"__    \n"
"\\ \\   \n"
" \\ \\  \n"
"  \\ \\ \n"
"   \\_\\\n"
"      "
)

Slant["]"] = (
"     ___\n"
"    /  /\n"
"    / / \n"
"   / /  \n"
" _/ /   \n"
"/__/    "
)

Slant["^"] = (
"  //|\n"
" |/||\n"
"  $  \n"
" $   \n"
"$    \n"
"     "
)

Slant["_"] = (
"       \n"
"       \n"
"       \n"
"       \n"
" ______\n"
"/_____/"
)

Slant["`"] = (
"  _ \n"
" ( )\n"
"  V \n"
" $  \n"
"$   \n"
"    "
)

Slant["a"] = (
"        \n"
"  ____ _\n"
" / __ `/\n"
"/ /_/ / \n"
"\\__,_/  \n"
"        "
)

Slant["b"] = (
"    __  \n"
"   / /_ \n"
"  / __ \\\n"
" / /_/ /\n"
"/_.___/ \n"
"        "
)

Slant["c"] = (
"       \n"
"  _____\n"
" / ___/\n"
"/ /__  \n"
"\\___/  \n"
"       "
)

Slant["d"] = (
"       __\n"
"  ____/ /\n"
" / __  / \n"
"/ /_/ /  \n"
"\\__,_/   \n"
"         "
)

Slant["e"] = (
"      \n"
"  ___ \n"
" / _ \\\n"
"/  __/\n"
"\\___/ \n"
"      "
)

Slant["f"] = (
"    ____\n"
"   / __/\n"
"  / /_  \n"
" / __/  \n"
"/_/     \n"
"        "
)

Slant["g"] = (
"         \n"
"   ____ _\n"
"  / __ `/\n"
" / /_/ / \n"
" \\__, /  \n"
"/____/   "
)

Slant["h"] = (
"    __  \n"
"   / /_ \n"
"  / __ \\\n"
" / / / /\n"
"/_/ /_/ \n"
"        "
)

Slant["i"] = (
"    _ \n"
"   (_)\n"
"  / / \n"
" / /  \n"
"/_/   \n"
"      "
)

Slant["j"] = (
"       _ \n"
"      (_)\n"
"     / / \n"
"    / /  \n"
" __/ /   \n"
"/___/    "
)

Slant["k"] = (
"    __  \n"
"   / /__\n"
"  / //_/\n"
" / ,<   \n"
"/_/|_|  \n"
"        "
)

Slant["l"] = (
"    __\n"
"   / /\n"
"  / / \n"
" / /  \n"
"/_/   \n"
"      "
)

Slant["m"] = (
"            \n"
"   ____ ___ \n"
"  / __ `__ \\\n"
" / / / / / /\n"
"/_/ /_/ /_/ \n"
"            "
)

Slant["n"] = (
"        \n"
"   ____ \n"
"  / __ \\\n"
" / / / /\n"
"/_/ /_/ \n"
"        "
)

Slant["o"] = (
"       \n"
"  ____ \n"
" / __ \\\n"
"/ /_/ /\n"
"\\____/ \n"
"       "
)

Slant["p"] = (
"         \n"
"    ____ \n"
"   / __ \\\n"
"  / /_/ /\n"
" / .___/ \n"
"/_/      "
)

Slant["q"] = (
"        \n"
"  ____ _\n"
" / __ `/\n"
"/ /_/ / \n"
"\\__, /  \n"
"  /_/   "
)

Slant["r"] = (
"        \n"
"   _____\n"
"  / ___/\n"
" / /    \n"
"/_/     \n"
"        "
)

Slant["s"] = (
"        \n"
"   _____\n"
"  / ___/\n"
" (__  ) \n"
"/____/  \n"
"        "
)

Slant["t"] = (
"   __ \n"
"  / /_\n"
" / __/\n"
"/ /_  \n"
"\\__/  \n"
"      "
)

Slant["u"] = (
"        \n"
"  __  __\n"
" / / / /\n"
"/ /_/ / \n"
"\\__,_/  \n"
"        "
)

Slant["v"] = (
"       \n"
" _   __\n"
"| | / /\n"
"| |/ / \n"
"|___/  \n"
"       "
)

Slant["w"] = (
"          \n"
" _      __\n"
"| | /| / /\n"
"| |/ |/ / \n"
"|__/|__/  \n"
"          "
)

Slant["x"] = (
"        \n"
"   _  __\n"
"  | |/_/\n"
" _>  <  \n"
"/_/|_|  \n"
"        "
)

Slant["y"] = (
"         \n"
"   __  __\n"
"  / / / /\n"
" / /_/ / \n"
" \\__, /  \n"
"/____/   "
)

Slant["z"] = (
"     \n"
" ____\n"
"/_  /\n"
" / /_\n"
"/___/\n"
"     "
)

Slant["{"] = (
"     __\n"
"   _/_/\n"
" _/_/  \n"
"< <    \n"
"/ /    \n"
"\\_\\    "
)

Slant["|"] = (
"     __\n"
"    / /\n"
"   / / \n"
"  / /  \n"
" / /   \n"
"/_/    "
)

Slant["}"] = (
"     _ \n"
"    | |\n"
"    / /\n"
"   _>_>\n"
" _/_/  \n"
"/_/    "
)

Slant["~"] = (
"  /\\//\n"
" //\\/ \n"
"  $   \n"
" $    \n"
"$     \n"
"      "
)
