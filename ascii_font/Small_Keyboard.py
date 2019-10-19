

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


Small_Keyboard = AsciiFont("$")
# flf2a$ 4 4 16 1 57


# smkeyboard.flf
# Adapted for figlet by Kent Nassen, kentn@cyberspace.org, 11/22/94, based
# on the idea:
# From: bas@damek.kth.se (Bas Meijer)
# Newsgroups: rec.arts.ascii
# Subject: Talk-line: keyboard.flf
# Date: 22 Nov 1994 07:26:10 -0600
# Organization: Royal Institute of Technology
# Lines: 41
# Sender: boba@gagme.wwa.com
# Approved: boba@wwa.com
# Message-ID: <3asrhi$con@gagme.wwa.com>
# References: <3asltp$aog@gagme.wwa.com>
# Reply-To: bas@damek.kth.se
# NNTP-Posting-Host: gagme.wwa.com
# In article aog@gagme.wwa.com, ssfiit@cs.umb.edu (SuperStreetFighter2Turbo) writes:
# >
# > I have composed a new figlet font! =)
# > it is called keyboard.flf. It resemble the actual keyboard, well, kinda! =)
# > anyway! here is a sample! =)
# >  _______ _______ _______ _______ _______ _______
# > |\     /|\     /|\     /|\     /|\     /|\     /|
# > | +---+ | +---+ | +---+ | +---+ | +---+ | +---+ |
# > | |   | | |   | | |   | | |   | | |   | | |   | |
# > | |s  | | |a  | | |m  | | |p  | | |l  | | |e  | |
# > | +---+ | +---+ | +---+ | +---+ | +---+ | +---+ |
# > |/_____\|/_____\|/_____\|/_____\|/_____\|/_____\|
#  ____ _________ ____ ____ ____ _________ ____ ____ ____ _________
# ||A |||       |||B |||I |||T |||       |||T |||O |||O |||       ||
# ||__|||_______|||__|||__|||__|||_______|||__|||__|||__|||_______||
# |/__\|/_______\|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/_______\|____
# ||B |||I |||G |||       |||I |||F |||       |||Y |||O |||U |||       ||
# ||__|||__|||__|||_______|||__|||__|||_______|||__|||__|||__|||_______||
# |/__\|/__\|/__\|/_______\|/__\|/__\|/_______\|/__\|/__\|/__\|/_______\|
# ||A |||S |||K |||       |||M |||E |||! |||       |||: |||) |||Return||
# ||__|||__|||__|||_______|||__|||__|||__|||_______|||__|||__|||      ||
# |/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/_______\|/__\|/__\|/l     ||
#                                                              l|_____||
# Bas.                                                         |/_____\|
# email: bas@damek.kth.se     ____  ____      KTH, Dept. of Mach. Design
#  _______  ___  ______      /    \/    \ ____________________________
# (       \/   \/      \    /            \       )   )   )      )     \
#  |   |   )    \   \___)  /              \  \__/\  /\   \  \__/   |   )
#  |      (  |   \_    \  (     (    )     )  )_ (  )_)   \  )_|      (
#  |   |   ) _    )\    )  \     \__/     /  /  \/  \     / /  \   \   \
# (_______/_/ \__/_____/    \     \/     /_______)___)___/______)__/\___)
#                            \____/\____/
# tel.: +46-(0)8-790 6308                     S-100 44 Stockholm, Sweden
Small_Keyboard[" "] = (
" _________ \n"
"||       ||\n"
"||_______||\n"
"|/_______\\|"
)

Small_Keyboard["!"] = (
" ____ \n"
"||! ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["\""] = (
" ____ \n"
"||\" ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["#"] = (
" ____ \n"
"||\n ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["$"] = (
" ____ \n"
"||$ ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["%"] = (
" ____ \n"
"||% ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["&"] = (
" ____ \n"
"||& ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["'"] = (
" ____ \n"
"||' ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["("] = (
" ____ \n"
"||( ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard[")"] = (
" ____ \n"
"||) ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["*"] = (
" ____ \n"
"||* ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["+"] = (
" ____ \n"
"||+ ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard[","] = (
" ____ \n"
"||, ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["-"] = (
" ____ \n"
"||- ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["."] = (
" ____ \n"
"||. ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["/"] = (
" ____ \n"
"||/ ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["0"] = (
" ____ \n"
"||0 ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["1"] = (
" ____ \n"
"||1 ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["2"] = (
" ____ \n"
"||2 ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["3"] = (
" ____ \n"
"||3 ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["4"] = (
" ____ \n"
"||4 ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["5"] = (
" ____ \n"
"||5 ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["6"] = (
" ____ \n"
"||6 ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["7"] = (
" ____ \n"
"||7 ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["8"] = (
" ____ \n"
"||8 ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["9"] = (
" ____ \n"
"||9 ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard[":"] = (
" ____ \n"
"||: ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard[";"] = (
" ____ \n"
"||; ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["<"] = (
" ____ \n"
"||< ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["="] = (
" ____ \n"
"||= ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard[">"] = (
" ____ \n"
"||> ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["?"] = (
" ____ \n"
"||? ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["@"] = (
" ____ \n"
"||\n ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["A"] = (
" ____ \n"
"||A ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["B"] = (
" ____ \n"
"||B ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["C"] = (
" ____ \n"
"||C ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["D"] = (
" ____ \n"
"||D ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["E"] = (
" ____ \n"
"||E ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["F"] = (
" ____ \n"
"||F ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["G"] = (
" ____ \n"
"||G ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["H"] = (
" ____ \n"
"||H ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["I"] = (
" ____ \n"
"||I ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["J"] = (
" ____ \n"
"||J ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["K"] = (
" ____ \n"
"||K ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["L"] = (
" ____ \n"
"||L ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["M"] = (
" ____ \n"
"||M ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["N"] = (
" ____ \n"
"||N ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["O"] = (
" ____ \n"
"||O ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["P"] = (
" ____ \n"
"||P ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["Q"] = (
" ____ \n"
"||Q ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["R"] = (
" ____ \n"
"||R ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["S"] = (
" ____ \n"
"||S ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["T"] = (
" ____ \n"
"||T ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["U"] = (
" ____ \n"
"||U ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["V"] = (
" ____ \n"
"||V ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["W"] = (
" ____ \n"
"||W ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["X"] = (
" ____ \n"
"||X ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["Y"] = (
" ____ \n"
"||Y ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["Z"] = (
" ____ \n"
"||Z ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["["] = (
" ____ \n"
"||[ ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["\\"] = (
" ____ \n"
"||\\ ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["]"] = (
" ____ \n"
"||] ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["^"] = (
" ____ \n"
"||^ ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["_"] = (
" ____ \n"
"||_ ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["`"] = (
" ____ \n"
"||` ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["a"] = (
" ____ \n"
"||a ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["b"] = (
" ____ \n"
"||b ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["c"] = (
" ____ \n"
"||c ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["d"] = (
" ____ \n"
"||d ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["e"] = (
" ____ \n"
"||e ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["f"] = (
" ____ \n"
"||f ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["g"] = (
" ____ \n"
"||g ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["h"] = (
" ____ \n"
"||h ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["i"] = (
" ____ \n"
"||i ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["j"] = (
" ____ \n"
"||j ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["k"] = (
" ____ \n"
"||k ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["l"] = (
" ____ \n"
"||l ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["m"] = (
" ____ \n"
"||m ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["n"] = (
" ____ \n"
"||n ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["o"] = (
" ____ \n"
"||o ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["p"] = (
" ____ \n"
"||p ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["q"] = (
" ____ \n"
"||q ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["r"] = (
" ____ \n"
"||r ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["s"] = (
" ____ \n"
"||s ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["t"] = (
" ____ \n"
"||t ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["u"] = (
" ____ \n"
"||u ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["v"] = (
" ____ \n"
"||v ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["w"] = (
" ____ \n"
"||w ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["x"] = (
" ____ \n"
"||x ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["y"] = (
" ____ \n"
"||y ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["z"] = (
" ____ \n"
"||z ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["{"] = (
" ____ \n"
"||{ ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["|"] = (
" ____ \n"
"||| ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["}"] = (
" ____ \n"
"||} ||\n"
"||__||\n"
"|/__\\|"
)

Small_Keyboard["~"] = (
" ____ \n"
"||~ ||\n"
"||__||\n"
"|/__\\|"
)

