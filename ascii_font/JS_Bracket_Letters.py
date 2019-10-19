

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


JS_Bracket_Letters = AsciiFont("$")
# flf2a$ 4 3 8 0 3


# Bracket Letters By Joan Stark
# Website: http://www.geocities.com/SoHo/7373/
# Figlet conversion by patorjk, April 17, 2008
JS_Bracket_Letters[" "] = (
"$ $\n"
"$ $\n"
"$ $\n"
"$ $"
)

JS_Bracket_Letters["!"] = (
"\n"
"\n"
"\n"
""
)

JS_Bracket_Letters["\""] = (
"\n"
"\n"
"\n"
""
)

JS_Bracket_Letters["#"] = (
"\n"
"\n"
"\n"
""
)

JS_Bracket_Letters["$"] = (
"\n"
"\n"
"\n"
""
)

JS_Bracket_Letters["%"] = (
"\n"
"\n"
"\n"
""
)

JS_Bracket_Letters["&"] = (
"\n"
"\n"
"\n"
""
)

JS_Bracket_Letters["'"] = (
"\n"
"\n"
"\n"
""
)

JS_Bracket_Letters["("] = (
"\n"
"\n"
"\n"
""
)

JS_Bracket_Letters[")"] = (
"\n"
"\n"
"\n"
""
)

JS_Bracket_Letters["*"] = (
"\n"
"\n"
"\n"
""
)

JS_Bracket_Letters["+"] = (
"\n"
"\n"
"\n"
""
)

JS_Bracket_Letters[","] = (
"\n"
"\n"
"\n"
""
)

JS_Bracket_Letters["-"] = (
"\n"
"\n"
"\n"
""
)

JS_Bracket_Letters["."] = (
"\n"
"\n"
"\n"
""
)

JS_Bracket_Letters["/"] = (
"\n"
"\n"
"\n"
""
)

JS_Bracket_Letters["0"] = (
"\n"
"\n"
"\n"
""
)

JS_Bracket_Letters["1"] = (
"\n"
"\n"
"\n"
""
)

JS_Bracket_Letters["2"] = (
"\n"
"\n"
"\n"
""
)

JS_Bracket_Letters["3"] = (
"\n"
"\n"
"\n"
""
)

JS_Bracket_Letters["4"] = (
"\n"
"\n"
"\n"
""
)

JS_Bracket_Letters["5"] = (
"\n"
"\n"
"\n"
""
)

JS_Bracket_Letters["6"] = (
"\n"
"\n"
"\n"
""
)

JS_Bracket_Letters["7"] = (
"\n"
"\n"
"\n"
""
)

JS_Bracket_Letters["8"] = (
"\n"
"\n"
"\n"
""
)

JS_Bracket_Letters["9"] = (
"\n"
"\n"
"\n"
""
)

JS_Bracket_Letters[":"] = (
"\n"
"\n"
"\n"
""
)

JS_Bracket_Letters[";"] = (
"\n"
"\n"
"\n"
""
)

JS_Bracket_Letters["<"] = (
"\n"
"\n"
"\n"
""
)

JS_Bracket_Letters["="] = (
"\n"
"\n"
"\n"
""
)

JS_Bracket_Letters[">"] = (
"\n"
"\n"
"\n"
""
)

JS_Bracket_Letters["?"] = (
"\n"
"\n"
"\n"
""
)

JS_Bracket_Letters["@"] = (
"\n"
"\n"
"\n"
""
)

JS_Bracket_Letters["A"] = (
"  .--.  \n"
" / {} \\ \n"
"/  /\\  \\\n"
"`-'  `-'"
)

JS_Bracket_Letters["B"] = (
".----. \n"
"| {}  }\n"
"| {}  }\n"
"`----' "
)

JS_Bracket_Letters["C"] = (
" .---. \n"
"/  ___}\n"
"\\     }\n"
" `---' "
)

JS_Bracket_Letters["D"] = (
".----. \n"
"| {}  \\\n"
"|     /\n"
"`----' "
)

JS_Bracket_Letters["E"] = (
".----.\n"
"| {_  \n"
"| {__ \n"
"`----'"
)

JS_Bracket_Letters["F"] = (
".----.\n"
"| {_  \n"
"| |   \n"
"`-'   "
)

JS_Bracket_Letters["G"] = (
" .---. \n"
"/   __}\n"
"\\  {_ }\n"
" `---' "
)

JS_Bracket_Letters["H"] = (
".-. .-.\n"
"| {_} |\n"
"| { } |\n"
"`-' `-'"
)

JS_Bracket_Letters["I"] = (
".-.\n"
"| |\n"
"| |\n"
"`-'"
)

JS_Bracket_Letters["J"] = (
"   .-.\n"
".-.| |\n"
"| {} |\n"
"`----'"
)

JS_Bracket_Letters["K"] = (
".-. .-.\n"
"| |/ / \n"
"| |\\ \\ \n"
"`-' `-'"
)

JS_Bracket_Letters["L"] = (
".-.   \n"
"| |   \n"
"| `--.\n"
"`----'"
)

JS_Bracket_Letters["M"] = (
".-.   .-.\n"
"|  `.'  |\n"
"| |\\ /| |\n"
"`-' ` `-'"
)

JS_Bracket_Letters["N"] = (
".-. .-.\n"
"|  `| |\n"
"| |\\  |\n"
"`-' `-'"
)

JS_Bracket_Letters["O"] = (
" .----. \n"
"/  {}  \\\n"
"\\      /\n"
" `----' "
)

JS_Bracket_Letters["P"] = (
".----. \n"
"| {}  }\n"
"| .--' \n"
"`-'    "
)

JS_Bracket_Letters["Q"] = (
" .----. \n"
"/  {}  \\\n"
"\\      /\n"
" `-----`"
)

JS_Bracket_Letters["R"] = (
".----. \n"
"| {}  }\n"
"| .-. \\\n"
"`-' `-'"
)

JS_Bracket_Letters["S"] = (
" .----.\n"
"{ {__  \n"
".-._} }\n"
"`----' "
)

JS_Bracket_Letters["T"] = (
" .---. \n"
"{_   _}\n"
"  | |  \n"
"  `-'  "
)

JS_Bracket_Letters["U"] = (
".-. .-.\n"
"| { } |\n"
"| {_} |\n"
"`-----'"
)

JS_Bracket_Letters["V"] = (
".-. .-.\n"
"| | | |\n"
"\\ \\_/ /\n"
" `---' "
)

JS_Bracket_Letters["W"] = (
".-. . .-.\n"
"| |/ \\| |\n"
"|  .'.  |\n"
"`-'   `-'"
)

JS_Bracket_Letters["X"] = (
".-.  .-.\n"
" \\ \\/ / \n"
" / /\\ \\ \n"
"`-'  `-'"
)

JS_Bracket_Letters["Y"] = (
".-.  .-.\n"
" \\ \\/ / \n"
"  }  {  \n"
"  `--'  "
)

JS_Bracket_Letters["Z"] = (
" .---. \n"
"{_   / \n"
" /    }\n"
" `---' "
)

JS_Bracket_Letters["["] = (
"\n"
"\n"
"\n"
""
)

JS_Bracket_Letters["\\"] = (
"\n"
"\n"
"\n"
""
)

JS_Bracket_Letters["]"] = (
"\n"
"\n"
"\n"
""
)

JS_Bracket_Letters["^"] = (
"\n"
"\n"
"\n"
""
)

JS_Bracket_Letters["_"] = (
"\n"
"\n"
"\n"
""
)

JS_Bracket_Letters["`"] = (
"\n"
"\n"
"\n"
""
)

JS_Bracket_Letters["a"] = (
"  .--.  \n"
" / {} \\ \n"
"/  /\\  \\\n"
"`-'  `-'"
)

JS_Bracket_Letters["b"] = (
".----. \n"
"| {}  }\n"
"| {}  }\n"
"`----' "
)

JS_Bracket_Letters["c"] = (
" .---. \n"
"/  ___}\n"
"\\     }\n"
" `---' "
)

JS_Bracket_Letters["d"] = (
".----. \n"
"| {}  \\\n"
"|     /\n"
"`----' "
)

JS_Bracket_Letters["e"] = (
".----.\n"
"| {_  \n"
"| {__ \n"
"`----'"
)

JS_Bracket_Letters["f"] = (
".----.\n"
"| {_  \n"
"| |   \n"
"`-'   "
)

JS_Bracket_Letters["g"] = (
" .---. \n"
"/   __}\n"
"\\  {_ }\n"
" `---' "
)

JS_Bracket_Letters["h"] = (
".-. .-.\n"
"| {_} |\n"
"| { } |\n"
"`-' `-'"
)

JS_Bracket_Letters["i"] = (
".-.\n"
"| |\n"
"| |\n"
"`-'"
)

JS_Bracket_Letters["j"] = (
"   .-.\n"
".-.| |\n"
"| {} |\n"
"`----'"
)

JS_Bracket_Letters["k"] = (
".-. .-.\n"
"| |/ / \n"
"| |\\ \\ \n"
"`-' `-'"
)

JS_Bracket_Letters["l"] = (
".-.   \n"
"| |   \n"
"| `--.\n"
"`----'"
)

JS_Bracket_Letters["m"] = (
".-.   .-.\n"
"|  `.'  |\n"
"| |\\ /| |\n"
"`-' ` `-'"
)

JS_Bracket_Letters["n"] = (
".-. .-.\n"
"|  `| |\n"
"| |\\  |\n"
"`-' `-'"
)

JS_Bracket_Letters["o"] = (
" .----. \n"
"/  {}  \\\n"
"\\      /\n"
" `----' "
)

JS_Bracket_Letters["p"] = (
".----. \n"
"| {}  }\n"
"| .--' \n"
"`-'    "
)

JS_Bracket_Letters["q"] = (
" .----. \n"
"/  {}  \\\n"
"\\      /\n"
" `-----`"
)

JS_Bracket_Letters["r"] = (
".----. \n"
"| {}  }\n"
"| .-. \\\n"
"`-' `-'"
)

JS_Bracket_Letters["s"] = (
" .----.\n"
"{ {__  \n"
".-._} }\n"
"`----' "
)

JS_Bracket_Letters["t"] = (
" .---. \n"
"{_   _}\n"
"  | |  \n"
"  `-'  "
)

JS_Bracket_Letters["u"] = (
".-. .-.\n"
"| { } |\n"
"| {_} |\n"
"`-----'"
)

JS_Bracket_Letters["v"] = (
".-. .-.\n"
"| | | |\n"
"\\ \\_/ /\n"
" `---' "
)

JS_Bracket_Letters["w"] = (
".-. . .-.\n"
"| |/ \\| |\n"
"|  .'.  |\n"
"`-'   `-'"
)

JS_Bracket_Letters["x"] = (
".-.  .-.\n"
" \\ \\/ / \n"
" / /\\ \\ \n"
"`-'  `-'"
)

JS_Bracket_Letters["y"] = (
".-.  .-.\n"
" \\ \\/ / \n"
"  }  {  \n"
"  `--'  "
)

JS_Bracket_Letters["z"] = (
" .---. \n"
"{_   / \n"
" /    }\n"
" `---' "
)

JS_Bracket_Letters["{"] = (
"\n"
"\n"
"\n"
""
)

JS_Bracket_Letters["|"] = (
"\n"
"\n"
"\n"
""
)

JS_Bracket_Letters["}"] = (
"\n"
"\n"
"\n"
""
)

JS_Bracket_Letters["~"] = (
"\n"
"\n"
"\n"
""
)

