

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


Small_Slant = AsciiFont("$")
# flf2a$ 5 4 14 15 10 0 22415


# SmSlant by Glenn Chappell 6/93 - based on Small & Slant
# Includes ISO Latin-1
# figlet release 2.1 -- 12 Aug 1994
# Permission is hereby given to modify this font, as long as the
# modifier's name is placed on a comment line.
# Modified by Paul Burton <solution@earthlink.net> 12/96 to include new parameter
# supported by FIGlet and FIGWin.  May also be slightly modified for better use
# of new full-width/kern/smush alternatives, but default output is NOT changed.
Small_Slant[" "] = (
"    $\n"
"   $ \n"
"  $  \n"
" $   \n"
"$    "
)

Small_Slant["!"] = (
"   __\n"
"  / /\n"
" /_/ \n"
"(_)  \n"
"     "
)

Small_Slant["\""] = (
" _ _ \n"
"( | )\n"
"|/|/ \n"
"$    \n"
"     "
)

Small_Slant["#"] = (
"     ____ \n"
"  __/ / /_\n"
" /_  . __/\n"
"/_    __/ \n"
" /_/_/    "
)

Small_Slant["$"] = (
"     \n"
"  _//\n"
" (_-<\n"
"/ __/\n"
"//   "
)

Small_Slant["%"] = (
" _   __\n"
"(_)_/_/\n"
" _/_/_ \n"
"/_/ (_)\n"
"       "
)

Small_Slant["&"] = (
"  ____   \n"
" / __/___\n"
" > _/_ _/\n"
"|_____/  \n"
"         "
)

Small_Slant["'"] = (
" _ \n"
"( )\n"
"|/ \n"
"$  \n"
"   "
)

Small_Slant["("] = (
"    __\n"
"  _/_/\n"
" / /  \n"
"/ /   \n"
"|_|   "
)

Small_Slant[")"] = (
"    _ \n"
"   | |\n"
"   / /\n"
" _/_/ \n"
"/_/   "
)

Small_Slant["*"] = (
"    \n"
" _/|\n"
"> _<\n"
"|/  \n"
"    "
)

Small_Slant["+"] = (
"    __ \n"
" __/ /_\n"
"/_  __/\n"
" /_/   \n"
"       "
)

Small_Slant[","] = (
"   \n"
"   \n"
" _ \n"
"( )\n"
"|/ "
)

Small_Slant["-"] = (
"     \n"
" ____\n"
"/___/\n"
" $   \n"
"     "
)

Small_Slant["."] = (
"   \n"
"   \n"
" _ \n"
"(_)\n"
"   "
)

Small_Slant["/"] = (
"     __\n"
"   _/_/\n"
" _/_/  \n"
"/_/    \n"
"       "
)

Small_Slant["0"] = (
"  ___ \n"
" / _ \\\n"
"/ // /\n"
"\\___/ \n"
"      "
)

Small_Slant["1"] = (
"  ___\n"
" <  /\n"
" / / \n"
"/_/  \n"
"     "
)

Small_Slant["2"] = (
"   ___ \n"
"  |_  |\n"
" / __/ \n"
"/____/ \n"
"       "
)

Small_Slant["3"] = (
"   ____\n"
"  |_  /\n"
" _/_ < \n"
"/____/ \n"
"       "
)

Small_Slant["4"] = (
"  ____\n"
" / / /\n"
"/_  _/\n"
" /_/  \n"
"      "
)

Small_Slant["5"] = (
"   ____\n"
"  / __/\n"
" /__ \\ \n"
"/____/ \n"
"       "
)

Small_Slant["6"] = (
"  ____\n"
" / __/\n"
"/ _ \\ \n"
"\\___/ \n"
"      "
)

Small_Slant["7"] = (
" ____\n"
"/_  /\n"
" / / \n"
"/_/  \n"
"     "
)

Small_Slant["8"] = (
"  ___ \n"
" ( _ )\n"
"/ _  |\n"
"\\___/ \n"
"      "
)

Small_Slant["9"] = (
"  ___ \n"
" / _ \\\n"
" \\_, /\n"
"/___/ \n"
"      "
)

Small_Slant[":"] = (
"   _ \n"
"  (_)\n"
" _   \n"
"(_)  \n"
"     "
)

Small_Slant[";"] = (
"   _ \n"
"  (_)\n"
" _   \n"
"( )  \n"
"|/   "
)

Small_Slant["<"] = (
"  __\n"
" / /\n"
"< < \n"
" \\_\\\n"
"    "
)

Small_Slant["="] = (
"      \n"
"  ____\n"
" /___/\n"
"/___/ \n"
"      "
)

Small_Slant[">"] = (
"__  \n"
"\\ \\ \n"
" > >\n"
"/_/ \n"
"    "
)

Small_Slant["?"] = (
" ___ \n"
"/__ \\\n"
" /__/\n"
"(_)  \n"
"     "
)

Small_Slant["@"] = (
"  _____ \n"
" / ___ \\\n"
"/ / _ `/\n"
"\\ \\_,_/ \n"
" \\___/  "
)

Small_Slant["A"] = (
"   ___ \n"
"  / _ |\n"
" / __ |\n"
"/_/ |_|\n"
"       "
)

Small_Slant["B"] = (
"   ___ \n"
"  / _ )\n"
" / _  |\n"
"/____/ \n"
"       "
)

Small_Slant["C"] = (
"  _____\n"
" / ___/\n"
"/ /__  \n"
"\\___/  \n"
"       "
)

Small_Slant["D"] = (
"   ___ \n"
"  / _ \\\n"
" / // /\n"
"/____/ \n"
"       "
)

Small_Slant["E"] = (
"   ____\n"
"  / __/\n"
" / _/  \n"
"/___/  \n"
"       "
)

Small_Slant["F"] = (
"   ____\n"
"  / __/\n"
" / _/  \n"
"/_/    \n"
"       "
)

Small_Slant["G"] = (
"  _____\n"
" / ___/\n"
"/ (_ / \n"
"\\___/  \n"
"       "
)

Small_Slant["H"] = (
"   __ __\n"
"  / // /\n"
" / _  / \n"
"/_//_/  \n"
"        "
)

Small_Slant["I"] = (
"   ____\n"
"  /  _/\n"
" _/ /  \n"
"/___/  \n"
"       "
)

Small_Slant["J"] = (
"     __\n"
" __ / /\n"
"/ // / \n"
"\\___/  \n"
"       "
)

Small_Slant["K"] = (
"   __ __\n"
"  / //_/\n"
" / ,<   \n"
"/_/|_|  \n"
"        "
)

Small_Slant["L"] = (
"   __ \n"
"  / / \n"
" / /__\n"
"/____/\n"
"      "
)

Small_Slant["M"] = (
"   __  ___\n"
"  /  |/  /\n"
" / /|_/ / \n"
"/_/  /_/  \n"
"          "
)

Small_Slant["N"] = (
"   _  __\n"
"  / |/ /\n"
" /    / \n"
"/_/|_/  \n"
"        "
)

Small_Slant["O"] = (
"  ____ \n"
" / __ \\\n"
"/ /_/ /\n"
"\\____/ \n"
"       "
)

Small_Slant["P"] = (
"   ___ \n"
"  / _ \\\n"
" / ___/\n"
"/_/    \n"
"       "
)

Small_Slant["Q"] = (
"  ____ \n"
" / __ \\\n"
"/ /_/ /\n"
"\\___\\_\\\n"
"       "
)

Small_Slant["R"] = (
"   ___ \n"
"  / _ \\\n"
" / , _/\n"
"/_/|_| \n"
"       "
)

Small_Slant["S"] = (
"   ____\n"
"  / __/\n"
" _\\ \\  \n"
"/___/  \n"
"       "
)

Small_Slant["T"] = (
" ______\n"
"/_  __/\n"
" / /   \n"
"/_/    \n"
"       "
)

Small_Slant["U"] = (
"  __  __\n"
" / / / /\n"
"/ /_/ / \n"
"\\____/  \n"
"        "
)

Small_Slant["V"] = (
"  _   __\n"
" | | / /\n"
" | |/ / \n"
" |___/  \n"
"        "
)

Small_Slant["W"] = (
"  _      __\n"
" | | /| / /\n"
" | |/ |/ / \n"
" |__/|__/  \n"
"           "
)

Small_Slant["X"] = (
"   _  __\n"
"  | |/_/\n"
" _>  <  \n"
"/_/|_|  \n"
"        "
)

Small_Slant["Y"] = (
" __  __\n"
" \\ \\/ /\n"
"  \\  / \n"
"  /_/  \n"
"       "
)

Small_Slant["Z"] = (
"  ____\n"
" /_  /\n"
"  / /_\n"
" /___/\n"
"      "
)

Small_Slant["["] = (
"    ___\n"
"   / _/\n"
"  / /  \n"
" / /   \n"
"/__/   "
)

Small_Slant["\\"] = (
"__   \n"
"\\ \\  \n"
" \\ \\ \n"
"  \\_\\\n"
"     "
)

Small_Slant["]"] = (
"    ___\n"
"   /  /\n"
"   / / \n"
" _/ /  \n"
"/__/   "
)

Small_Slant["^"] = (
" //|\n"
"|/||\n"
" $  \n"
"$   \n"
"    "
)

Small_Slant["_"] = (
"     \n"
"     \n"
"     \n"
" ____\n"
"/___/"
)

Small_Slant["`"] = (
" _ \n"
"( )\n"
" V \n"
"$  \n"
"   "
)

Small_Slant["a"] = (
"      \n"
" ___ _\n"
"/ _ `/\n"
"\\_,_/ \n"
"      "
)

Small_Slant["b"] = (
"   __ \n"
"  / / \n"
" / _ \\\n"
"/_.__/\n"
"      "
)

Small_Slant["c"] = (
"     \n"
" ____\n"
"/ __/\n"
"\\__/ \n"
"     "
)

Small_Slant["d"] = (
"     __\n"
" ___/ /\n"
"/ _  / \n"
"\\_,_/  \n"
"       "
)

Small_Slant["e"] = (
"     \n"
" ___ \n"
"/ -_)\n"
"\\__/ \n"
"     "
)

Small_Slant["f"] = (
"   ___\n"
"  / _/\n"
" / _/ \n"
"/_/   \n"
"      "
)

Small_Slant["g"] = (
"       \n"
"  ___ _\n"
" / _ `/\n"
" \\_, / \n"
"/___/  "
)

Small_Slant["h"] = (
"   __ \n"
"  / / \n"
" / _ \\\n"
"/_//_/\n"
"      "
)

Small_Slant["i"] = (
"   _ \n"
"  (_)\n"
" / / \n"
"/_/  \n"
"     "
)

Small_Slant["j"] = (
"      _ \n"
"     (_)\n"
"    / / \n"
" __/ /  \n"
"|___/   "
)

Small_Slant["k"] = (
"   __  \n"
"  / /__\n"
" /  '_/\n"
"/_/\\_\\ \n"
"       "
)

Small_Slant["l"] = (
"   __\n"
"  / /\n"
" / / \n"
"/_/  \n"
"     "
)

Small_Slant["m"] = (
"       \n"
"  __ _ \n"
" /  ' \\\n"
"/_/_/_/\n"
"       "
)

Small_Slant["n"] = (
"      \n"
"  ___ \n"
" / _ \\\n"
"/_//_/\n"
"      "
)

Small_Slant["o"] = (
"     \n"
" ___ \n"
"/ _ \\\n"
"\\___/\n"
"     "
)

Small_Slant["p"] = (
"       \n"
"   ___ \n"
"  / _ \\\n"
" / .__/\n"
"/_/    "
)

Small_Slant["q"] = (
"      \n"
" ___ _\n"
"/ _ `/\n"
"\\_, / \n"
" /_/  "
)

Small_Slant["r"] = (
"      \n"
"  ____\n"
" / __/\n"
"/_/   \n"
"      "
)

Small_Slant["s"] = (
"     \n"
"  ___\n"
" (_-<\n"
"/___/\n"
"     "
)

Small_Slant["t"] = (
"  __ \n"
" / /_\n"
"/ __/\n"
"\\__/ \n"
"     "
)

Small_Slant["u"] = (
"      \n"
" __ __\n"
"/ // /\n"
"\\_,_/ \n"
"      "
)

Small_Slant["v"] = (
"      \n"
" _  __\n"
"| |/ /\n"
"|___/ \n"
"      "
)

Small_Slant["w"] = (
"        \n"
" _    __\n"
"| |/|/ /\n"
"|__,__/ \n"
"        "
)

Small_Slant["x"] = (
"      \n"
" __ __\n"
" \\ \\ /\n"
"/_\\_\\ \n"
"      "
)

Small_Slant["y"] = (
"       \n"
"  __ __\n"
" / // /\n"
" \\_, / \n"
"/___/  "
)

Small_Slant["z"] = (
"    \n"
" ___\n"
"/_ /\n"
"/__/\n"
"    "
)

Small_Slant["{"] = (
"    __\n"
"  _/_/\n"
"_/ /  \n"
"/ /   \n"
"\\_\\   "
)

Small_Slant["|"] = (
"    __\n"
"   / /\n"
"  / / \n"
" / /  \n"
"/_/   "
)

Small_Slant["}"] = (
"   __  \n"
"   \\ \\ \n"
"   / /_\n"
" _/_/  \n"
"/_/    "
)

Small_Slant["~"] = (
" /\\//\n"
"//\\/ \n"
" $   \n"
"$    \n"
"     "
)

