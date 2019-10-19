

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


Small_Isometric1 = AsciiFont("$")
# flf2a$ 7 7 18 -1 18


# smisome1.flf
# Downsized version of isometric1.flf - M. Lindsey (mglindse@nyx.cs.du.edu)
# February 24, 1996
# ---
# isometric1.flf
# Figlet conversion by Kent Nassen (kentn@cyberspace.org), 8-10-94, based
# on the fonts posted by Lennert Stock:
# From: stock@fwi.uva.nl (Lennert Stock)
# Date: 15 Jul 1994 00:04:25 GMT
# Here are some fonts. Non-figlet I'm afraid, if you wanna convert them, be
# my guest. I posted the isometric fonts before.
# ------------------------------------------------------------------------------
#                  --------- L e n n e r t   S t o c k
#                                   stock@fwi.uva.nl --------
Small_Isometric1[" "] = (
"$   $\n"
"$   $\n"
"$   $\n"
"$   $\n"
"$   $\n"
"$   $\n"
"$   $"
)

Small_Isometric1["!"] = (
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
""
)

Small_Isometric1["\""] = (
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
""
)

Small_Isometric1["#"] = (
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
""
)

Small_Isometric1["$"] = (
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
""
)

Small_Isometric1["%"] = (
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
""
)

Small_Isometric1["&"] = (
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
""
)

Small_Isometric1["'"] = (
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
""
)

Small_Isometric1["("] = (
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
""
)

Small_Isometric1[")"] = (
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
""
)

Small_Isometric1["*"] = (
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
""
)

Small_Isometric1["+"] = (
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
""
)

Small_Isometric1[","] = (
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
""
)

Small_Isometric1["-"] = (
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
""
)

Small_Isometric1["."] = (
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
""
)

Small_Isometric1["/"] = (
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
""
)

Small_Isometric1["0"] = (
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
""
)

Small_Isometric1["1"] = (
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
""
)

Small_Isometric1["2"] = (
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
""
)

Small_Isometric1["3"] = (
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
""
)

Small_Isometric1["4"] = (
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
""
)

Small_Isometric1["5"] = (
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
""
)

Small_Isometric1["6"] = (
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
""
)

Small_Isometric1["7"] = (
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
""
)

Small_Isometric1["8"] = (
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
""
)

Small_Isometric1["9"] = (
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
""
)

Small_Isometric1[":"] = (
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
""
)

Small_Isometric1[";"] = (
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
""
)

Small_Isometric1["<"] = (
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
""
)

Small_Isometric1["="] = (
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
""
)

Small_Isometric1[">"] = (
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
""
)

Small_Isometric1["?"] = (
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
""
)

Small_Isometric1["@"] = (
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
""
)

Small_Isometric1["A"] = (
"    ___   \n"
"   /\\  \\  \n"
"  /::\\  \\ \n"
" /::\\:\\__\\\n"
" \\/\\::/  /\n"
"   /:/  / \n"
"   \\/__/  "
)

Small_Isometric1["B"] = (
"    ___   \n"
"   /\\  \\  \n"
"  /::\\  \\ \n"
" /::\\:\\__\\\n"
" \\:\\::/  /\n"
"  \\::/  / \n"
"   \\/__/  "
)

Small_Isometric1["C"] = (
"    ___   \n"
"   /\\  \\  \n"
"  /::\\  \\ \n"
" /:/\\:\\__\\\n"
" \\:\\ \\/__/\n"
"  \\:\\__\\  \n"
"   \\/__/  "
)

Small_Isometric1["D"] = (
"    ___   \n"
"   /\\  \\  \n"
"  /::\\  \\ \n"
" /:/\\:\\__\\\n"
" \\:\\/:/  /\n"
"  \\::/  / \n"
"   \\/__/  "
)

Small_Isometric1["E"] = (
"    ___   \n"
"   /\\  \\  \n"
"  /::\\  \\ \n"
" /::\\:\\__\\\n"
" \\:\\:\\/  /\n"
"  \\:\\/  / \n"
"   \\/__/  "
)

Small_Isometric1["F"] = (
"    ___   \n"
"   /\\  \\  \n"
"  /::\\  \\ \n"
" /::\\:\\__\\\n"
" \\/\\:\\/__/\n"
"    \\/__/ \n"
"          "
)

Small_Isometric1["G"] = (
"    ___   \n"
"   /\\  \\  \n"
"  /::\\  \\ \n"
" /:/\\:\\__\\\n"
" \\:\\:\\/__/\n"
"  \\::/  / \n"
"   \\/__/  "
)

Small_Isometric1["H"] = (
"    ___   \n"
"   /\\__\\  \n"
"  /:/__/_ \n"
" /::\\/\\__\\\n"
" \\/\\::/  /\n"
"   /:/  / \n"
"   \\/__/  "
)

Small_Isometric1["I"] = (
"    ___   \n"
"   /\\  \\  \n"
"  _\\:\\  \\ \n"
" /\\/::\\__\\\n"
" \\::/\\/__/\n"
"  \\:\\__\\  \n"
"   \\/__/  "
)

Small_Isometric1["J"] = (
"    ___   \n"
"   /\\  \\  \n"
"  _\\:\\  \\ \n"
" /\\/::\\__\\\n"
" \\::/\\/__/\n"
"  \\/__/   \n"
"          "
)

Small_Isometric1["K"] = (
"    ___   \n"
"   /\\__\\  \n"
"  /:/ _/_ \n"
" /::-\"\\__\\\n"
" \\;:;-\",-\"\n"
"  |:|  |  \n"
"   \\|__|  "
)

Small_Isometric1["L"] = (
"    ___   \n"
"   /\\__\\  \n"
"  /:/  /  \n"
" /:/__/   \n"
" \\:\\  \\   \n"
"  \\:\\__\\  \n"
"   \\/__/  "
)

Small_Isometric1["M"] = (
"    ___   \n"
"   /\\__\\  \n"
"  /::L_L_ \n"
" /:/L:\\__\\\n"
" \\/_/:/  /\n"
"   /:/  / \n"
"   \\/__/  "
)

Small_Isometric1["N"] = (
"    ___   \n"
"   /\\__\\  \n"
"  /:| _|_ \n"
" /::|/\\__\\\n"
" \\/|::/  /\n"
"   |:/  / \n"
"   \\/__/  "
)

Small_Isometric1["O"] = (
"    ___   \n"
"   /\\  \\  \n"
"  /::\\  \\ \n"
" /:/\\:\\__\\\n"
" \\:\\/:/  /\n"
"  \\::/  / \n"
"   \\/__/  "
)

Small_Isometric1["P"] = (
"    ___   \n"
"   /\\  \\  \n"
"  /::\\  \\ \n"
" /::\\:\\__\\\n"
" \\/\\::/  /\n"
"    \\/__/ \n"
"          "
)

Small_Isometric1["Q"] = (
"    ___   \n"
"   /\\  \\  \n"
"  /::\\  \\ \n"
"  \\:\\:\\__\\\n"
"   \\::/  /\n"
"   /:/  / \n"
"   \\/__/  "
)

Small_Isometric1["R"] = (
"    ___   \n"
"   /\\  \\  \n"
"  /::\\  \\ \n"
" /::\\:\\__\\\n"
" \\;:::/  /\n"
"  |:\\/__/ \n"
"   \\|__|  "
)

Small_Isometric1["S"] = (
"    ___   \n"
"   /\\  \\  \n"
"  /::\\  \\ \n"
" /\\:\\:\\__\\\n"
" \\:\\:\\/__/\n"
"  \\::/  / \n"
"   \\/__/  "
)

Small_Isometric1["T"] = (
"    ___   \n"
"   /\\  \\  \n"
"   \\:\\  \\ \n"
"   /::\\__\\\n"
"  /:/\\/__/\n"
"  \\/__/   \n"
"          "
)

Small_Isometric1["U"] = (
"    ___   \n"
"   /\\__\\  \n"
"  /:/ _/_ \n"
" /:/_/\\__\\\n"
" \\:\\/:/  /\n"
"  \\::/  / \n"
"   \\/__/  "
)

Small_Isometric1["V"] = (
"    ___   \n"
"   /\\__\\  \n"
"  /:/ _/_ \n"
" |::L/\\__\\\n"
" |::::/  /\n"
"  L;;/__/ \n"
"          "
)

Small_Isometric1["W"] = (
"    ___   \n"
"   /\\__\\  \n"
"  /:/\\__\\ \n"
" /:/:/\\__\\\n"
" \\::/:/  /\n"
"  \\::/  / \n"
"   \\/__/  "
)

Small_Isometric1["X"] = (
"    ___   \n"
"   /\\__\\  \n"
"  |::L__L \n"
" /::::\\__\\\n"
" \\;::;/__/\n"
"  |::|__| \n"
"   \\/__/  "
)

Small_Isometric1["Y"] = (
"    ___   \n"
"   /\\__\\  \n"
"  |::L__L \n"
"  |:::\\__\\\n"
"  /:;;/__/\n"
"  \\/__/   \n"
"          "
)

Small_Isometric1["Z"] = (
"    ___   \n"
"   /\\  \\  \n"
"  _\\:\\  \\ \n"
" /::::\\__\\\n"
" \\::;;/__/\n"
"  \\:\\__\\  \n"
"   \\/__/  "
)

Small_Isometric1["["] = (
"    ___   \n"
"   /\\  \\  \n"
"  /::\\  \\ \n"
" /:LS:\\__\\\n"
" \\1994/  /\n"
"  \\::/  / \n"
"   \\/__/  "
)

Small_Isometric1["\\"] = (
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
""
)

Small_Isometric1["]"] = (
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
""
)

Small_Isometric1["^"] = (
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
""
)

Small_Isometric1["_"] = (
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
""
)

Small_Isometric1["`"] = (
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
""
)

Small_Isometric1["a"] = (
"    ___   \n"
"   /\\  \\  \n"
"  /::\\  \\ \n"
" /::\\:\\__\\\n"
" \\/\\::/  /\n"
"   /:/  / \n"
"   \\/__/  "
)

Small_Isometric1["b"] = (
"    ___   \n"
"   /\\  \\  \n"
"  /::\\  \\ \n"
" /::\\:\\__\\\n"
" \\:\\::/  /\n"
"  \\::/  / \n"
"   \\/__/  "
)

Small_Isometric1["c"] = (
"    ___   \n"
"   /\\  \\  \n"
"  /::\\  \\ \n"
" /:/\\:\\__\\\n"
" \\:\\ \\/__/\n"
"  \\:\\__\\  \n"
"   \\/__/  "
)

Small_Isometric1["d"] = (
"    ___   \n"
"   /\\  \\  \n"
"  /::\\  \\ \n"
" /:/\\:\\__\\\n"
" \\:\\/:/  /\n"
"  \\::/  / \n"
"   \\/__/  "
)

Small_Isometric1["e"] = (
"    ___   \n"
"   /\\  \\  \n"
"  /::\\  \\ \n"
" /::\\:\\__\\\n"
" \\:\\:\\/  /\n"
"  \\:\\/  / \n"
"   \\/__/  "
)

Small_Isometric1["f"] = (
"    ___   \n"
"   /\\  \\  \n"
"  /::\\  \\ \n"
" /::\\:\\__\\\n"
" \\/\\:\\/__/\n"
"    \\/__/ \n"
"          "
)

Small_Isometric1["g"] = (
"    ___   \n"
"   /\\  \\  \n"
"  /::\\  \\ \n"
" /:/\\:\\__\\\n"
" \\:\\:\\/__/\n"
"  \\::/  / \n"
"   \\/__/  "
)

Small_Isometric1["h"] = (
"    ___   \n"
"   /\\__\\  \n"
"  /:/__/_ \n"
" /::\\/\\__\\\n"
" \\/\\::/  /\n"
"   /:/  / \n"
"   \\/__/  "
)

Small_Isometric1["i"] = (
"    ___   \n"
"   /\\  \\  \n"
"  _\\:\\  \\ \n"
" /\\/::\\__\\\n"
" \\::/\\/__/\n"
"  \\:\\__\\  \n"
"   \\/__/  "
)

Small_Isometric1["j"] = (
"    ___   \n"
"   /\\  \\  \n"
"  _\\:\\  \\ \n"
" /\\/::\\__\\\n"
" \\::/\\/__/\n"
"  \\/__/   \n"
"          "
)

Small_Isometric1["k"] = (
"    ___   \n"
"   /\\__\\  \n"
"  /:/ _/_ \n"
" /::-\"\\__\\\n"
" \\;:;-\",-\"\n"
"  |:|  |  \n"
"   \\|__|  "
)

Small_Isometric1["l"] = (
"    ___   \n"
"   /\\__\\  \n"
"  /:/  /  \n"
" /:/__/   \n"
" \\:\\  \\   \n"
"  \\:\\__\\  \n"
"   \\/__/  "
)

Small_Isometric1["m"] = (
"    ___   \n"
"   /\\__\\  \n"
"  /::L_L_ \n"
" /:/L:\\__\\\n"
" \\/_/:/  /\n"
"   /:/  / \n"
"   \\/__/  "
)

Small_Isometric1["n"] = (
"    ___   \n"
"   /\\__\\  \n"
"  /:| _|_ \n"
" /::|/\\__\\\n"
" \\/|::/  /\n"
"   |:/  / \n"
"   \\/__/  "
)

Small_Isometric1["o"] = (
"    ___   \n"
"   /\\  \\  \n"
"  /::\\  \\ \n"
" /:/\\:\\__\\\n"
" \\:\\/:/  /\n"
"  \\::/  / \n"
"   \\/__/  "
)

Small_Isometric1["p"] = (
"    ___   \n"
"   /\\  \\  \n"
"  /::\\  \\ \n"
" /::\\:\\__\\\n"
" \\/\\::/  /\n"
"    \\/__/ \n"
"          "
)

Small_Isometric1["q"] = (
"    ___   \n"
"   /\\  \\  \n"
"  /::\\  \\ \n"
"  \\:\\:\\__\\\n"
"   \\::/  /\n"
"   /:/  / \n"
"   \\/__/  "
)

Small_Isometric1["r"] = (
"    ___   \n"
"   /\\  \\  \n"
"  /::\\  \\ \n"
" /::\\:\\__\\\n"
" \\;:::/  /\n"
"  |:\\/__/ \n"
"   \\|__|  "
)

Small_Isometric1["s"] = (
"    ___   \n"
"   /\\  \\  \n"
"  /::\\  \\ \n"
" /\\:\\:\\__\\\n"
" \\:\\:\\/__/\n"
"  \\::/  / \n"
"   \\/__/  "
)

Small_Isometric1["t"] = (
"    ___   \n"
"   /\\  \\  \n"
"   \\:\\  \\ \n"
"   /::\\__\\\n"
"  /:/\\/__/\n"
"  \\/__/   \n"
"          "
)

Small_Isometric1["u"] = (
"    ___   \n"
"   /\\__\\  \n"
"  /:/ _/_ \n"
" /:/_/\\__\\\n"
" \\:\\/:/  /\n"
"  \\::/  / \n"
"   \\/__/  "
)

Small_Isometric1["v"] = (
"    ___   \n"
"   /\\__\\  \n"
"  /:/ _/_ \n"
" |::L/\\__\\\n"
" |::::/  /\n"
"  L;;/__/ \n"
"          "
)

Small_Isometric1["w"] = (
"    ___   \n"
"   /\\__\\  \n"
"  /:/\\__\\ \n"
" /:/:/\\__\\\n"
" \\::/:/  /\n"
"  \\::/  / \n"
"   \\/__/  "
)

Small_Isometric1["x"] = (
"    ___   \n"
"   /\\__\\  \n"
"  |::L__L \n"
" /::::\\__\\\n"
" \\;::;/__/\n"
"  |::|__| \n"
"   \\/__/  "
)

Small_Isometric1["y"] = (
"    ___   \n"
"   /\\__\\  \n"
"  |::L__L \n"
"  |:::\\__\\\n"
"  /:;;/__/\n"
"  \\/__/   \n"
"          "
)

Small_Isometric1["z"] = (
"    ___   \n"
"   /\\  \\  \n"
"  _\\:\\  \\ \n"
" /::::\\__\\\n"
" \\::;;/__/\n"
"  \\:\\__\\  \n"
"   \\/__/  "
)

Small_Isometric1["{"] = (
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
""
)

Small_Isometric1["|"] = (
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
""
)

Small_Isometric1["}"] = (
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
""
)

Small_Isometric1["~"] = (
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
""
)

