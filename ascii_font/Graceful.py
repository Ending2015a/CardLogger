

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


Graceful = AsciiFont("$")
# flf2a$ 4 4 8 0 14 0 8256


# Graceful-6x4 by Mikhael Goikhman, http://migo.n3.net/, 20/Jan/2002.
# Why did I make this font? Most of the figlet fonts are ugly for my taste.
# Chars ".", "'" or "|" are not as graceful as "(", ")", "/", "\" and "_".
# Also most of the fonts unlike this one are either small or good, not both.
# And finally, I wanted to have a strictly sized font, this one is 6x4.
# I intended to create this elegant figlet font in 1996, but only in
# January 2002 actually had the time to bring it to the working state. :)
# Cyrillic letters are supported, maybe somewhen I will add hebrew latters.
# To get a monospaced font 6x4, use "figlet -f graceful -m -1". Enjoy!
# Permission is hereby given to modify this font, as long as the
# modifier's name is added to this comment.
Graceful[" "] = (
"$$    \n"
"$$    \n"
"$$    \n"
"$$    "
)

Graceful["!"] = (
"  _   \n"
" / \\  \n"
" \\_/  \n"
" (_)  "
)

Graceful["\""] = (
"  _ _ \n"
" (/(/ \n"
"      \n"
"      "
)

Graceful["#"] = (
" _  _ \n"
"/ )( \\\n"
")    (\n"
"\\_)(_/"
)

Graceful["$"] = (
" ____ \n"
"/ (__)\n"
"\\__  \\\n"
"(__)_/"
)

Graceful["%"] = (
" _ _  \n"
"(// ) \n"
" / /_ \n"
"(_/(/ "
)

Graceful["&"] = (
"  ___ \n"
" ( _ \\\n"
"/ _  /\n"
"\\__\\_)"
)

Graceful["'"] = (
"   _  \n"
"  (/  \n"
"      \n"
"      "
)

Graceful["("] = (
"   _  \n"
"  / ) \n"
" ( (  \n"
"  \\_) "
)

Graceful[")"] = (
"  _   \n"
" ( \\  \n"
"  ) ) \n"
" (_/  "
)

Graceful["*"] = (
"      \n"
"(\\/\\/)\n"
" )  ( \n"
"(/\\/\\)"
)

Graceful["+"] = (
"  _   \n"
" ( )  \n"
"(_ _) \n"
" (_)  "
)

Graceful[","] = (
"      \n"
"  _   \n"
" ( )  \n"
" (/   "
)

Graceful["-"] = (
"      \n"
" ___  \n"
"(___) \n"
"      "
)

Graceful["."] = (
"      \n"
"      \n"
"  _   \n"
" (_)  "
)

Graceful["/"] = (
"   _  \n"
"  / ) \n"
" / /  \n"
"(_/   "
)

Graceful["0"] = (
"  __  \n"
" /  \\ \n"
"(  0 )\n"
" \\__/ "
)

Graceful["1"] = (
"  __  \n"
" /  \\ \n"
"(_/ / \n"
" (__) "
)

Graceful["2"] = (
" ____ \n"
"(___ \\\n"
" / __/\n"
"(____)"
)

Graceful["3"] = (
" ____ \n"
"( __ \\\n"
" (__ (\n"
"(____/"
)

Graceful["4"] = (
"  ___ \n"
" / _ \\\n"
"(__  (\n"
"  (__/"
)

Graceful["5"] = (
"  ___ \n"
" / __)\n"
"(___ \\\n"
"(____/"
)

Graceful["6"] = (
"  ___ \n"
" / __)\n"
"(  _ \\\n"
" \\___/"
)

Graceful["7"] = (
" ____ \n"
"(__  )\n"
"  / / \n"
" (_/  "
)

Graceful["8"] = (
" ____ \n"
"/ _  \\\n"
") _  (\n"
"\\____/"
)

Graceful["9"] = (
" ___  \n"
"/ _ \\ \n"
"\\__  )\n"
"(___/ "
)

Graceful[":"] = (
"  _   \n"
" (_)  \n"
"  _   \n"
" (_)  "
)

Graceful[";"] = (
"  _   \n"
" (_)  \n"
" ( )  \n"
" (/   "
)

Graceful["<"] = (
"   __ \n"
"  / / \n"
" ( (  \n"
"  \\_\\ "
)

Graceful["="] = (
" ___  \n"
"(___) \n"
" ___  \n"
"(___) "
)

Graceful[">"] = (
" __   \n"
" \\ \\  \n"
"  ) ) \n"
" /_/  "
)

Graceful["?"] = (
" ___  \n"
"(__ \\ \n"
" (__/ \n"
" (_)  "
)

Graceful["@"] = (
"  ___ \n"
" /   \\\n"
"( (__/\n"
" \\___)"
)

Graceful["A"] = (
"  __  \n"
" / _\\ \n"
"/    \\\n"
"\\_/\\_/"
)

Graceful["B"] = (
" ____ \n"
"(  _ \\\n"
" ) _ (\n"
"(____/"
)

Graceful["C"] = (
"  ___ \n"
" / __)\n"
"( (__ \n"
" \\___)"
)

Graceful["D"] = (
" ____ \n"
"(    \\\n"
" ) D (\n"
"(____/"
)

Graceful["E"] = (
" ____ \n"
"(  __)\n"
" ) _) \n"
"(____)"
)

Graceful["F"] = (
" ____ \n"
"(  __)\n"
" ) _) \n"
"(__)  "
)

Graceful["G"] = (
"  ___ \n"
" / __)\n"
"( (_ \\\n"
" \\___/"
)

Graceful["H"] = (
" _  _ \n"
"/ )( \\\n"
") __ (\n"
"\\_)(_/"
)

Graceful["I"] = (
"  __  \n"
" (  ) \n"
"  )(  \n"
" (__) "
)

Graceful["J"] = (
"   __ \n"
" _(  )\n"
"/ \\) \\\n"
"\\____/"
)

Graceful["K"] = (
" __ _ \n"
"(  / )\n"
" )  ( \n"
"(__\\_)"
)

Graceful["L"] = (
" __   \n"
"(  )  \n"
"/ (_/\\\n"
"\\____/"
)

Graceful["M"] = (
" _  _ \n"
"( \\/ )\n"
"/ \\/ \\\n"
"\\_)(_/"
)

Graceful["N"] = (
" __ _ \n"
"(  ( \\\n"
"/    /\n"
"\\_)__)"
)

Graceful["O"] = (
"  __  \n"
" /  \\ \n"
"(  O )\n"
" \\__/ "
)

Graceful["P"] = (
" ____ \n"
"(  _ \\\n"
" ) __/\n"
"(__)  "
)

Graceful["Q"] = (
"  __  \n"
" /  \\ \n"
"(  O )\n"
" \\__\\)"
)

Graceful["R"] = (
" ____ \n"
"(  _ \\\n"
" )   /\n"
"(__\\_)"
)

Graceful["S"] = (
" ____ \n"
"/ ___)\n"
"\\___ \\\n"
"(____/"
)

Graceful["T"] = (
" ____ \n"
"(_  _)\n"
"  )(  \n"
" (__) "
)

Graceful["U"] = (
" _  _ \n"
"/ )( \\\n"
") \\/ (\n"
"\\____/"
)

Graceful["V"] = (
" _  _ \n"
"/ )( \\\n"
"\\ \\/ /\n"
" \\__/ "
)

Graceful["W"] = (
" _  _ \n"
"/ )( \\\n"
"\\ /\\ /\n"
"(_/\\_)"
)

Graceful["X"] = (
" _  _ \n"
"( \\/ )\n"
" )  ( \n"
"(_/\\_)"
)

Graceful["Y"] = (
" _  _ \n"
"( \\/ )\n"
" )  / \n"
"(__/  "
)

Graceful["Z"] = (
" ____ \n"
"(__  )\n"
" / _/ \n"
"(____)"
)

Graceful["["] = (
" ___  \n"
"/  _) \n"
") (_  \n"
"\\___) "
)

Graceful["\\"] = (
" _    \n"
"( \\   \n"
" \\ \\  \n"
"  \\_) "
)

Graceful["]"] = (
"  ___ \n"
" (_  \\\n"
"  _) (\n"
" (___/"
)

Graceful["^"] = (
"  __  \n"
" /  \\ \n"
"(_/\\_)\n"
"      "
)

Graceful["_"] = (
"      \n"
"      \n"
" ____ \n"
"(____)"
)

Graceful["`"] = (
"  _   \n"
"  \\)  \n"
"      \n"
"      "
)

Graceful["a"] = (
"  __  \n"
" / _\\ \n"
"/    \\\n"
"\\_/\\_/"
)

Graceful["b"] = (
" ____ \n"
"(  _ \\\n"
" ) _ (\n"
"(____/"
)

Graceful["c"] = (
"  ___ \n"
" / __)\n"
"( (__ \n"
" \\___)"
)

Graceful["d"] = (
" ____ \n"
"(    \\\n"
" ) D (\n"
"(____/"
)

Graceful["e"] = (
" ____ \n"
"(  __)\n"
" ) _) \n"
"(____)"
)

Graceful["f"] = (
" ____ \n"
"(  __)\n"
" ) _) \n"
"(__)  "
)

Graceful["g"] = (
"  ___ \n"
" / __)\n"
"( (_ \\\n"
" \\___/"
)

Graceful["h"] = (
" _  _ \n"
"/ )( \\\n"
") __ (\n"
"\\_)(_/"
)

Graceful["i"] = (
"  __  \n"
" (  ) \n"
"  )(  \n"
" (__) "
)

Graceful["j"] = (
"   __ \n"
" _(  )\n"
"/ \\) \\\n"
"\\____/"
)

Graceful["k"] = (
" __ _ \n"
"(  / )\n"
" )  ( \n"
"(__\\_)"
)

Graceful["l"] = (
" __   \n"
"(  )  \n"
"/ (_/\\\n"
"\\____/"
)

Graceful["m"] = (
" _  _ \n"
"( \\/ )\n"
"/ \\/ \\\n"
"\\_)(_/"
)

Graceful["n"] = (
" __ _ \n"
"(  ( \\\n"
"/    /\n"
"\\_)__)"
)

Graceful["o"] = (
"  __  \n"
" /  \\ \n"
"(  O )\n"
" \\__/ "
)

Graceful["p"] = (
" ____ \n"
"(  _ \\\n"
" ) __/\n"
"(__)  "
)

Graceful["q"] = (
"  __  \n"
" /  \\ \n"
"(  O )\n"
" \\__\\)"
)

Graceful["r"] = (
" ____ \n"
"(  _ \\\n"
" )   /\n"
"(__\\_)"
)

Graceful["s"] = (
" ____ \n"
"/ ___)\n"
"\\___ \\\n"
"(____/"
)

Graceful["t"] = (
" ____ \n"
"(_  _)\n"
"  )(  \n"
" (__) "
)

Graceful["u"] = (
" _  _ \n"
"/ )( \\\n"
") \\/ (\n"
"\\____/"
)

Graceful["v"] = (
" _  _ \n"
"/ )( \\\n"
"\\ \\/ /\n"
" \\__/ "
)

Graceful["w"] = (
" _  _ \n"
"/ )( \\\n"
"\\ /\\ /\n"
"(_/\\_)"
)

Graceful["x"] = (
" _  _ \n"
"( \\/ )\n"
" )  ( \n"
"(_/\\_)"
)

Graceful["y"] = (
" _  _ \n"
"( \\/ )\n"
" )  / \n"
"(__/  "
)

Graceful["z"] = (
" ____ \n"
"(__  )\n"
" / _/ \n"
"(____)"
)

Graceful["{"] = (
"  ___ \n"
" (  _)\n"
"(_ (_ \n"
" (___)"
)

Graceful["|"] = (
"  _   \n"
" ( \\  \n"
" / /  \n"
" \\_)  "
)

Graceful["}"] = (
" ___  \n"
"(_  ) \n"
" _) _)\n"
"(___) "
)

Graceful["~"] = (
" __   \n"
"(_ \\_ \n"
"  \\__)\n"
"      "
)

