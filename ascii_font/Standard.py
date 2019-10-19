

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


Standard = AsciiFont("$")
# flf2a$ 6 5 16 15 13 0 24463 229


# Standard by Glenn Chappell & Ian Chai 3/93 -- based on Frank's .sig
# Includes ISO Latin-1
# figlet release 2.1 -- 12 Aug 1994
# Modified for figlet 2.2 by John Cowan <cowan@ccil.org>
#   to add Latin-{2,3,4,5} support (Unicode U+0100-017F).
# Permission is hereby given to modify this font, as long as the
# modifier's name is placed on a comment line.
# Modified by Paul Burton <solution@earthlink.net> 12/96 to include new parameter
# supported by FIGlet and FIGWin.  May also be slightly modified for better use
# of new full-width/kern/smush alternatives, but default output is NOT changed.
# Font modified May 20, 2012 by patorjk to add the 0xCA0 character
Standard[" "] = (
" $\n"
" $\n"
" $\n"
" $\n"
" $\n"
" $"
)

Standard["!"] = (
"  _ \n"
" | |\n"
" | |\n"
" |_|\n"
" (_)\n"
"    "
)

Standard["\""] = (
"  _ _ \n"
" ( | )\n"
"  V V \n"
"   $  \n"
"   $  \n"
"      "
)

Standard["#"] = (
"    _  _   \n"
"  _| || |_ \n"
" |_  ..  _|\n"
" |_      _|\n"
"   |_||_|  \n"
"           "
)

Standard["$"] = (
"   _  \n"
"  | | \n"
" / __)\n"
" \\__ \\\n"
" (   /\n"
"  |_| "
)

Standard["%"] = (
"  _  __\n"
" (_)/ /\n"
"   / / \n"
"  / /_ \n"
" /_/(_)\n"
"       "
)

Standard["&"] = (
"   ___   \n"
"  ( _ )  \n"
"  / _ \\/\\\n"
" | (_>  <\n"
"  \\___/\\/\n"
"         "
)

Standard["'"] = (
"  _ \n"
" ( )\n"
" |/ \n"
"  $ \n"
"  $ \n"
"    "
)

Standard["("] = (
"   __\n"
"  / /\n"
" | | \n"
" | | \n"
" | | \n"
"  \\_\\"
)

Standard[")"] = (
" __  \n"
" \\ \\ \n"
"  | |\n"
"  | |\n"
"  | |\n"
" /_/ "
)

Standard["*"] = (
"       \n"
" __/\\__\n"
" \\    /\n"
" /_  _\\\n"
"   \\/  \n"
"       "
)

Standard["+"] = (
"        \n"
"    _   \n"
"  _| |_ \n"
" |_   _|\n"
"   |_|  \n"
"        "
)

Standard[","] = (
"    \n"
"    \n"
"    \n"
"  _ \n"
" ( )\n"
" |/ "
)

Standard["-"] = (
"        \n"
"        \n"
"  _____ \n"
" |_____|\n"
"    $   \n"
"        "
)

Standard["."] = (
"    \n"
"    \n"
"    \n"
"  _ \n"
" (_)\n"
"    "
)

Standard["/"] = (
"     __\n"
"    / /\n"
"   / / \n"
"  / /  \n"
" /_/   \n"
"       "
)

Standard["0"] = (
"   ___  \n"
"  / _ \\ \n"
" | | | |\n"
" | |_| |\n"
"  \\___/ \n"
"        "
)

Standard["1"] = (
"  _ \n"
" / |\n"
" | |\n"
" | |\n"
" |_|\n"
"    "
)

Standard["2"] = (
"  ____  \n"
" |___ \\ \n"
"   __) |\n"
"  / __/ \n"
" |_____|\n"
"        "
)

Standard["3"] = (
"  _____ \n"
" |___ / \n"
"   |_ \\ \n"
"  ___) |\n"
" |____/ \n"
"        "
)

Standard["4"] = (
"  _  _   \n"
" | || |  \n"
" | || |_ \n"
" |__   _|\n"
"    |_|  \n"
"         "
)

Standard["5"] = (
"  ____  \n"
" | ___| \n"
" |___ \\ \n"
"  ___) |\n"
" |____/ \n"
"        "
)

Standard["6"] = (
"   __   \n"
"  / /_  \n"
" | '_ \\ \n"
" | (_) |\n"
"  \\___/ \n"
"        "
)

Standard["7"] = (
"  _____ \n"
" |___  |\n"
"    / / \n"
"   / /  \n"
"  /_/   \n"
"        "
)

Standard["8"] = (
"   ___  \n"
"  ( _ ) \n"
"  / _ \\ \n"
" | (_) |\n"
"  \\___/ \n"
"        "
)

Standard["9"] = (
"   ___  \n"
"  / _ \\ \n"
" | (_) |\n"
"  \\__, |\n"
"    /_/ \n"
"        "
)

Standard[":"] = (
"    \n"
"  _ \n"
" (_)\n"
"  _ \n"
" (_)\n"
"    "
)

Standard[";"] = (
"    \n"
"  _ \n"
" (_)\n"
"  _ \n"
" ( )\n"
" |/ "
)

Standard["<"] = (
"   __\n"
"  / /\n"
" / / \n"
" \\ \\ \n"
"  \\_\\\n"
"     "
)

Standard["="] = (
"        \n"
"  _____ \n"
" |_____|\n"
" |_____|\n"
"    $   \n"
"        "
)

Standard[">"] = (
" __  \n"
" \\ \\ \n"
"  \\ \\\n"
"  / /\n"
" /_/ \n"
"     "
)

Standard["?"] = (
"  ___ \n"
" |__ \\\n"
"   / /\n"
"  |_| \n"
"  (_) \n"
"      "
)

Standard["@"] = (
"    ____  \n"
"   / __ \\ \n"
"  / / _` |\n"
" | | (_| |\n"
"  \\ \\__,_|\n"
"   \\____/ "
)

Standard["A"] = (
"     _    \n"
"    / \\   \n"
"   / _ \\  \n"
"  / ___ \\ \n"
" /_/   \\_\\\n"
"          "
)

Standard["B"] = (
"  ____  \n"
" | __ ) \n"
" |  _ \\ \n"
" | |_) |\n"
" |____/ \n"
"        "
)

Standard["C"] = (
"   ____ \n"
"  / ___|\n"
" | |    \n"
" | |___ \n"
"  \\____|\n"
"        "
)

Standard["D"] = (
"  ____  \n"
" |  _ \\ \n"
" | | | |\n"
" | |_| |\n"
" |____/ \n"
"        "
)

Standard["E"] = (
"  _____ \n"
" | ____|\n"
" |  _|  \n"
" | |___ \n"
" |_____|\n"
"        "
)

Standard["F"] = (
"  _____ \n"
" |  ___|\n"
" | |_   \n"
" |  _|  \n"
" |_|    \n"
"        "
)

Standard["G"] = (
"   ____ \n"
"  / ___|\n"
" | |  _ \n"
" | |_| |\n"
"  \\____|\n"
"        "
)

Standard["H"] = (
"  _   _ \n"
" | | | |\n"
" | |_| |\n"
" |  _  |\n"
" |_| |_|\n"
"        "
)

Standard["I"] = (
"  ___ \n"
" |_ _|\n"
"  | | \n"
"  | | \n"
" |___|\n"
"      "
)

Standard["J"] = (
"      _ \n"
"     | |\n"
"  _  | |\n"
" | |_| |\n"
"  \\___/ \n"
"        "
)

Standard["K"] = (
"  _  __\n"
" | |/ /\n"
" | ' / \n"
" | . \\ \n"
" |_|\\_\\\n"
"       "
)

Standard["L"] = (
"  _     \n"
" | |    \n"
" | |    \n"
" | |___ \n"
" |_____|\n"
"        "
)

Standard["M"] = (
"  __  __ \n"
" |  \\/  |\n"
" | |\\/| |\n"
" | |  | |\n"
" |_|  |_|\n"
"         "
)

Standard["N"] = (
"  _   _ \n"
" | \\ | |\n"
" |  \\| |\n"
" | |\\  |\n"
" |_| \\_|\n"
"        "
)

Standard["O"] = (
"   ___  \n"
"  / _ \\ \n"
" | | | |\n"
" | |_| |\n"
"  \\___/ \n"
"        "
)

Standard["P"] = (
"  ____  \n"
" |  _ \\ \n"
" | |_) |\n"
" |  __/ \n"
" |_|    \n"
"        "
)

Standard["Q"] = (
"   ___  \n"
"  / _ \\ \n"
" | | | |\n"
" | |_| |\n"
"  \\__\\_\\\n"
"        "
)

Standard["R"] = (
"  ____  \n"
" |  _ \\ \n"
" | |_) |\n"
" |  _ < \n"
" |_| \\_\\\n"
"        "
)

Standard["S"] = (
"  ____  \n"
" / ___| \n"
" \\___ \\ \n"
"  ___) |\n"
" |____/ \n"
"        "
)

Standard["T"] = (
"  _____ \n"
" |_   _|\n"
"   | |  \n"
"   | |  \n"
"   |_|  \n"
"        "
)

Standard["U"] = (
"  _   _ \n"
" | | | |\n"
" | | | |\n"
" | |_| |\n"
"  \\___/ \n"
"        "
)

Standard["V"] = (
" __     __\n"
" \\ \\   / /\n"
"  \\ \\ / / \n"
"   \\ V /  \n"
"    \\_/   \n"
"          "
)

Standard["W"] = (
" __        __\n"
" \\ \\      / /\n"
"  \\ \\ /\\ / / \n"
"   \\ V  V /  \n"
"    \\_/\\_/   \n"
"             "
)

Standard["X"] = (
" __  __\n"
" \\ \\/ /\n"
"  \\  / \n"
"  /  \\ \n"
" /_/\\_\\\n"
"       "
)

Standard["Y"] = (
" __   __\n"
" \\ \\ / /\n"
"  \\ V / \n"
"   | |  \n"
"   |_|  \n"
"        "
)

Standard["Z"] = (
"  _____\n"
" |__  /\n"
"   / / \n"
"  / /_ \n"
" /____|\n"
"       "
)

Standard["["] = (
"  __ \n"
" | _|\n"
" | | \n"
" | | \n"
" | | \n"
" |__|"
)

Standard["\\"] = (
" __    \n"
" \\ \\   \n"
"  \\ \\  \n"
"   \\ \\ \n"
"    \\_\\\n"
"       "
)

Standard["]"] = (
"  __ \n"
" |_ |\n"
"  | |\n"
"  | |\n"
"  | |\n"
" |__|"
)

Standard["^"] = (
"  /\\ \n"
" |/\\|\n"
"   $ \n"
"   $ \n"
"   $ \n"
"     "
)

Standard["_"] = (
"        \n"
"        \n"
"        \n"
"        \n"
"  _____ \n"
" |_____|"
)

Standard["`"] = (
"  _ \n"
" ( )\n"
"  \\|\n"
"  $ \n"
"  $ \n"
"    "
)

Standard["a"] = (
"        \n"
"   __ _ \n"
"  / _` |\n"
" | (_| |\n"
"  \\__,_|\n"
"        "
)

Standard["b"] = (
"  _     \n"
" | |__  \n"
" | '_ \\ \n"
" | |_) |\n"
" |_.__/ \n"
"        "
)

Standard["c"] = (
"       \n"
"   ___ \n"
"  / __|\n"
" | (__ \n"
"  \\___|\n"
"       "
)

Standard["d"] = (
"      _ \n"
"   __| |\n"
"  / _` |\n"
" | (_| |\n"
"  \\__,_|\n"
"        "
)

Standard["e"] = (
"       \n"
"   ___ \n"
"  / _ \\\n"
" |  __/\n"
"  \\___|\n"
"       "
)

Standard["f"] = (
"   __ \n"
"  / _|\n"
" | |_ \n"
" |  _|\n"
" |_|  \n"
"      "
)

Standard["g"] = (
"        \n"
"   __ _ \n"
"  / _` |\n"
" | (_| |\n"
"  \\__, |\n"
"  |___/ "
)

Standard["h"] = (
"  _     \n"
" | |__  \n"
" | '_ \\ \n"
" | | | |\n"
" |_| |_|\n"
"        "
)

Standard["i"] = (
"  _ \n"
" (_)\n"
" | |\n"
" | |\n"
" |_|\n"
"    "
)

Standard["j"] = (
"    _ \n"
"   (_)\n"
"   | |\n"
"   | |\n"
"  _/ |\n"
" |__/ "
)

Standard["k"] = (
"  _    \n"
" | | __\n"
" | |/ /\n"
" |   < \n"
" |_|\\_\\\n"
"       "
)

Standard["l"] = (
"  _ \n"
" | |\n"
" | |\n"
" | |\n"
" |_|\n"
"    "
)

Standard["m"] = (
"            \n"
"  _ __ ___  \n"
" | '_ ` _ \\ \n"
" | | | | | |\n"
" |_| |_| |_|\n"
"            "
)

Standard["n"] = (
"        \n"
"  _ __  \n"
" | '_ \\ \n"
" | | | |\n"
" |_| |_|\n"
"        "
)

Standard["o"] = (
"        \n"
"   ___  \n"
"  / _ \\ \n"
" | (_) |\n"
"  \\___/ \n"
"        "
)

Standard["p"] = (
"        \n"
"  _ __  \n"
" | '_ \\ \n"
" | |_) |\n"
" | .__/ \n"
" |_|    "
)

Standard["q"] = (
"        \n"
"   __ _ \n"
"  / _` |\n"
" | (_| |\n"
"  \\__, |\n"
"     |_|"
)

Standard["r"] = (
"       \n"
"  _ __ \n"
" | '__|\n"
" | |   \n"
" |_|   \n"
"       "
)

Standard["s"] = (
"      \n"
"  ___ \n"
" / __|\n"
" \\__ \\\n"
" |___/\n"
"      "
)

Standard["t"] = (
"  _   \n"
" | |_ \n"
" | __|\n"
" | |_ \n"
"  \\__|\n"
"      "
)

Standard["u"] = (
"        \n"
"  _   _ \n"
" | | | |\n"
" | |_| |\n"
"  \\__,_|\n"
"        "
)

Standard["v"] = (
"        \n"
" __   __\n"
" \\ \\ / /\n"
"  \\ V / \n"
"   \\_/  \n"
"        "
)

Standard["w"] = (
"           \n"
" __      __\n"
" \\ \\ /\\ / /\n"
"  \\ V  V / \n"
"   \\_/\\_/  \n"
"           "
)

Standard["x"] = (
"       \n"
" __  __\n"
" \\ \\/ /\n"
"  >  < \n"
" /_/\\_\\\n"
"       "
)

Standard["y"] = (
"        \n"
"  _   _ \n"
" | | | |\n"
" | |_| |\n"
"  \\__, |\n"
"  |___/ "
)

Standard["z"] = (
"      \n"
"  ____\n"
" |_  /\n"
"  / / \n"
" /___|\n"
"      "
)

Standard["{"] = (
"    __\n"
"   / /\n"
"  | | \n"
" < <  \n"
"  | | \n"
"   \\_\\"
)

Standard["|"] = (
"  _ \n"
" | |\n"
" | |\n"
" | |\n"
" | |\n"
" |_|"
)

Standard["}"] = (
" __   \n"
" \\ \\  \n"
"  | | \n"
"   > >\n"
"  | | \n"
" /_/  "
)

Standard["~"] = (
"  /\\/|\n"
" |/\\/ \n"
"   $  \n"
"   $  \n"
"   $  \n"
"      "
)

