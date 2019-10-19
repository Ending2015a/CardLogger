

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


Rectangles = AsciiFont("$")
# flf2a$ 6 5 15 1 1


# rectangles.flf by David Villegas <mnementh@netcom.com> 12/94
Rectangles[" "] = (
"$$\n"
"$$\n"
"$$\n"
"$$\n"
"$$\n"
"$$"
)

Rectangles["!"] = (
" __ \n"
"|  |\n"
"|  |\n"
"|__|\n"
"|__|\n"
"    "
)

Rectangles["\""] = (
" _ _ \n"
"| | |\n"
"|_|_|\n"
" $$$ \n"
" $$$ \n"
" $$$ "
)

Rectangles["#"] = (
"   _ _   \n"
" _| | |_ \n"
"|_     _|\n"
"|_     _|\n"
"  |_|_|  \n"
"         "
)

Rectangles["$"] = (
"   _   \n"
" _| |_ \n"
"|   __|\n"
"|__   |\n"
"|_   _|\n"
"  |_|  "
)

Rectangles["%"] = (
"       \n"
" __ __ \n"
"|__|  |\n"
"|   __|\n"
"|__|__|\n"
"       "
)

Rectangles["&"] = (
"   _   \n"
" _| |_ \n"
"|   __|\n"
"|   __|\n"
"|_   _|\n"
"  |_|  "
)

Rectangles["'"] = (
" _ \n"
"| |\n"
"|_|\n"
" $ \n"
" $ \n"
" $ "
)

Rectangles["("] = (
"   _ \n"
" _|_|\n"
"| |  \n"
"| |  \n"
"|_|_ \n"
"  |_|"
)

Rectangles[")"] = (
" _   \n"
"|_|_ \n"
"  | |\n"
"  | |\n"
" _|_|\n"
"|_|  "
)

Rectangles["*"] = (
"       \n"
" _____ \n"
"| | | |\n"
"|-   -|\n"
"|_|_|_|\n"
"       "
)

Rectangles["+"] = (
"       \n"
"   _   \n"
" _| |_ \n"
"|_   _|\n"
"  |_|  \n"
"       "
)

Rectangles[","] = (
" $ \n"
" $ \n"
" $ \n"
" _ \n"
"| |\n"
"|_|"
)

Rectangles["-"] = (
" $$$ \n"
" $$$ \n"
" ___ \n"
"|___|\n"
" $$$ \n"
" $$$ "
)

Rectangles["."] = (
" $ \n"
" $ \n"
" $ \n"
" _ \n"
"|_|\n"
" $ "
)

Rectangles["/"] = (
"     \n"
"   _ \n"
"  / |\n"
" / / \n"
"|_/  \n"
"     "
)

Rectangles["0"] = (
"     \n"
" ___ \n"
"|   |\n"
"| | |\n"
"|___|\n"
"     "
)

Rectangles["1"] = (
"       \n"
" ___   \n"
"|_  |  \n"
" _| |_ \n"
"|_____|\n"
"       "
)

Rectangles["2"] = (
"     \n"
" ___ \n"
"|_  |\n"
"|  _|\n"
"|___|\n"
"     "
)

Rectangles["3"] = (
"     \n"
" ___ \n"
"|_  |\n"
"|_  |\n"
"|___|\n"
"     "
)

Rectangles["4"] = (
"     \n"
" ___ \n"
"| | |\n"
"|_  |\n"
"  |_|\n"
"     "
)

Rectangles["5"] = (
"     \n"
" ___ \n"
"|  _|\n"
"|_  |\n"
"|___|\n"
"     "
)

Rectangles["6"] = (
"     \n"
" ___ \n"
"|  _|\n"
"| . |\n"
"|___|\n"
"     "
)

Rectangles["7"] = (
"     \n"
" ___ \n"
"|_  |\n"
"  | |\n"
"  |_|\n"
"     "
)

Rectangles["8"] = (
"     \n"
" ___ \n"
"| . |\n"
"| . |\n"
"|___|\n"
"     "
)

Rectangles["9"] = (
"     \n"
" ___ \n"
"| . |\n"
"|_  |\n"
"|___|\n"
"     "
)

Rectangles[":"] = (
"   \n"
" _ \n"
"|_|\n"
" _ \n"
"|_|\n"
"   "
)

Rectangles[";"] = (
"   \n"
" _ \n"
"|_|\n"
" _ \n"
"| |\n"
"|_|"
)

Rectangles["<"] = (
"   __\n"
"  / /\n"
" / / \n"
"< <  \n"
" \\ \\ \n"
"  \\_\\"
)

Rectangles["="] = (
" $$$$$ \n"
" $$$$$ \n"
" _____ \n"
"|_____|\n"
"|_____|\n"
" $$$$$ "
)

Rectangles[">"] = (
"__   \n"
"\\ \\  \n"
" \\ \\ \n"
"  > >\n"
" / / \n"
"/_/  "
)

Rectangles["?"] = (
" _____ \n"
"|___  |\n"
"  |  _|\n"
"  |_|  \n"
"  |_|  \n"
"       "
)

Rectangles["@"] = (
"       \n"
" _____ \n"
"|  __ |\n"
"| |___|\n"
"|_____|\n"
"       "
)

Rectangles["A"] = (
"       \n"
" _____ \n"
"|  _  |\n"
"|     |\n"
"|__|__|\n"
"       "
)

Rectangles["B"] = (
"       \n"
" _____ \n"
"| __  |\n"
"| __ -|\n"
"|_____|\n"
"       "
)

Rectangles["C"] = (
"       \n"
" _____ \n"
"|     |\n"
"|   --|\n"
"|_____|\n"
"       "
)

Rectangles["D"] = (
"       \n"
" ____  \n"
"|    \\ \n"
"|  |  |\n"
"|____/ \n"
"       "
)

Rectangles["E"] = (
"       \n"
" _____ \n"
"|   __|\n"
"|   __|\n"
"|_____|\n"
"       "
)

Rectangles["F"] = (
"       \n"
" _____ \n"
"|   __|\n"
"|   __|\n"
"|__|   \n"
"       "
)

Rectangles["G"] = (
"       \n"
" _____ \n"
"|   __|\n"
"|  |  |\n"
"|_____|\n"
"       "
)

Rectangles["H"] = (
"       \n"
" _____ \n"
"|  |  |\n"
"|     |\n"
"|__|__|\n"
"       "
)

Rectangles["I"] = (
"       \n"
" _____ \n"
"|     |\n"
"|-   -|\n"
"|_____|\n"
"       "
)

Rectangles["J"] = (
"       \n"
"    __ \n"
" __|  |\n"
"|  |  |\n"
"|_____|\n"
"       "
)

Rectangles["K"] = (
"       \n"
" _____ \n"
"|  |  |\n"
"|    -|\n"
"|__|__|\n"
"       "
)

Rectangles["L"] = (
"       \n"
" __    \n"
"|  |   \n"
"|  |__ \n"
"|_____|\n"
"       "
)

Rectangles["M"] = (
"       \n"
" _____ \n"
"|     |\n"
"| | | |\n"
"|_|_|_|\n"
"       "
)

Rectangles["N"] = (
"       \n"
" _____ \n"
"|   | |\n"
"| | | |\n"
"|_|___|\n"
"       "
)

Rectangles["O"] = (
"       \n"
" _____ \n"
"|     |\n"
"|  |  |\n"
"|_____|\n"
"       "
)

Rectangles["P"] = (
"       \n"
" _____ \n"
"|  _  |\n"
"|   __|\n"
"|__|   \n"
"       "
)

Rectangles["Q"] = (
"       \n"
" _____ \n"
"|     |\n"
"|  |  |\n"
"|__  _|\n"
"   |__|"
)

Rectangles["R"] = (
"       \n"
" _____ \n"
"| __  |\n"
"|    -|\n"
"|__|__|\n"
"       "
)

Rectangles["S"] = (
"       \n"
" _____ \n"
"|   __|\n"
"|__   |\n"
"|_____|\n"
"       "
)

Rectangles["T"] = (
"       \n"
" _____ \n"
"|_   _|\n"
"  | |  \n"
"  |_|  \n"
"       "
)

Rectangles["U"] = (
"       \n"
" _____ \n"
"|  |  |\n"
"|  |  |\n"
"|_____|\n"
"       "
)

Rectangles["V"] = (
"       \n"
" _____ \n"
"|  |  |\n"
"|  |  |\n"
" \\___/ \n"
"       "
)

Rectangles["W"] = (
"       \n"
" _ _ _ \n"
"| | | |\n"
"| | | |\n"
"|_____|\n"
"       "
)

Rectangles["X"] = (
"       \n"
" __ __ \n"
"|  |  |\n"
"|-   -|\n"
"|__|__|\n"
"       "
)

Rectangles["Y"] = (
"       \n"
" __ __ \n"
"|  |  |\n"
"|_   _|\n"
"  |_|  \n"
"       "
)

Rectangles["Z"] = (
"       \n"
" _____ \n"
"|__   |\n"
"|   __|\n"
"|_____|\n"
"       "
)

Rectangles["["] = (
" ___ \n"
"|  _|\n"
"| |  \n"
"| |  \n"
"| |_ \n"
"|___|"
)

Rectangles["\\"] = (
"     \n"
" _   \n"
"| \\  \n"
" \\ \\ \n"
"  \\_|\n"
"     "
)

Rectangles["]"] = (
" ___ \n"
"|_  |\n"
"  | |\n"
"  | |\n"
" _| |\n"
"|___|"
)

Rectangles["^"] = (
" _____ \n"
"|  _  |\n"
"|_| |_|\n"
" $$$$$ \n"
" $$$$$ \n"
" $$$$$ "
)

Rectangles["_"] = (
" $$$$$ \n"
" $$$$$ \n"
" $$$$$ \n"
" $$$$$ \n"
" _____ \n"
"|_____|"
)

Rectangles["`"] = (
" ___ \n"
"|_  |\n"
"  |_|\n"
" $$$ \n"
" $$$ \n"
" $$$ "
)

Rectangles["a"] = (
"     \n"
"     \n"
" ___ \n"
"| .'|\n"
"|__,|\n"
"     "
)

Rectangles["b"] = (
"     \n"
" _   \n"
"| |_ \n"
"| . |\n"
"|___|\n"
"     "
)

Rectangles["c"] = (
"     \n"
"     \n"
" ___ \n"
"|  _|\n"
"|___|\n"
"     "
)

Rectangles["d"] = (
"     \n"
"   _ \n"
" _| |\n"
"| . |\n"
"|___|\n"
"     "
)

Rectangles["e"] = (
"     \n"
"     \n"
" ___ \n"
"| -_|\n"
"|___|\n"
"     "
)

Rectangles["f"] = (
"     \n"
" ___ \n"
"|  _|\n"
"|  _|\n"
"|_|  \n"
"     "
)

Rectangles["g"] = (
"     \n"
"     \n"
" ___ \n"
"| . |\n"
"|_  |\n"
"|___|"
)

Rectangles["h"] = (
"     \n"
" _   \n"
"| |_ \n"
"|   |\n"
"|_|_|\n"
"     "
)

Rectangles["i"] = (
"   \n"
" _ \n"
"|_|\n"
"| |\n"
"|_|\n"
"   "
)

Rectangles["j"] = (
"     \n"
"   _ \n"
"  |_|\n"
"  | |\n"
" _| |\n"
"|___|"
)

Rectangles["k"] = (
"     \n"
" _   \n"
"| |_ \n"
"| '_|\n"
"|_,_|\n"
"     "
)

Rectangles["l"] = (
"   \n"
" _ \n"
"| |\n"
"| |\n"
"|_|\n"
"   "
)

Rectangles["m"] = (
"       \n"
"       \n"
" _____ \n"
"|     |\n"
"|_|_|_|\n"
"       "
)

Rectangles["n"] = (
"     \n"
"     \n"
" ___ \n"
"|   |\n"
"|_|_|\n"
"     "
)

Rectangles["o"] = (
"     \n"
"     \n"
" ___ \n"
"| . |\n"
"|___|\n"
"     "
)

Rectangles["p"] = (
"     \n"
"     \n"
" ___ \n"
"| . |\n"
"|  _|\n"
"|_|  "
)

Rectangles["q"] = (
"     \n"
"     \n"
" ___ \n"
"| . |\n"
"|_  |\n"
"  |_|"
)

Rectangles["r"] = (
"     \n"
"     \n"
" ___ \n"
"|  _|\n"
"|_|  \n"
"     "
)

Rectangles["s"] = (
"     \n"
"     \n"
" ___ \n"
"|_ -|\n"
"|___|\n"
"     "
)

Rectangles["t"] = (
"     \n"
" _   \n"
"| |_ \n"
"|  _|\n"
"|_|  \n"
"     "
)

Rectangles["u"] = (
"     \n"
"     \n"
" _ _ \n"
"| | |\n"
"|___|\n"
"     "
)

Rectangles["v"] = (
"     \n"
"     \n"
" _ _ \n"
"| | |\n"
" \\_/ \n"
"     "
)

Rectangles["w"] = (
"       \n"
"       \n"
" _ _ _ \n"
"| | | |\n"
"|_____|\n"
"       "
)

Rectangles["x"] = (
"     \n"
"     \n"
" _ _ \n"
"|_'_|\n"
"|_,_|\n"
"     "
)

Rectangles["y"] = (
"     \n"
"     \n"
" _ _ \n"
"| | |\n"
"|_  |\n"
"|___|"
)

Rectangles["z"] = (
"     \n"
"     \n"
" ___ \n"
"|- _|\n"
"|___|\n"
"     "
)

Rectangles["{"] = (
"   ___ \n"
"  |  _|\n"
" _| |  \n"
"|_  |  \n"
"  | |_ \n"
"  |___|"
)

Rectangles["|"] = (
" _ \n"
"| |\n"
"| |\n"
"| |\n"
"| |\n"
"|_|"
)

Rectangles["}"] = (
" ___   \n"
"|_  |  \n"
"  | |_ \n"
"  |  _|\n"
" _| |  \n"
"|___|  "
)

Rectangles["~"] = (
" _____ \n"
"|   | |\n"
"|_|___|\n"
" $$$$$ \n"
" $$$$$ \n"
" $$$$$ "
)

