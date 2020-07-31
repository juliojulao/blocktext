blocks = {
    '#': '█',

    '`': '▀',

    '-': '▄',

    '=': '■',

    '_': '░',

    ' ': ' ',
}

letters = {
    'A':["#``#",
         "#``#",
         "`__`",
        ],

    'B':["#``=",
         "#``=",
         "```_",
        ],

    'C':["#```",
         "#___",
         "````",
        ],

    'D':["#``-",
         "#__#",
         "```_"
        ],

    'E':["#```",
         "#```",
         "````",
        ],

    'F':["#```",
         "#``_",
         "`___",
        ],

    'G':["#```",
         "#_`#",
         "````",
        ],

    'H':["#__#",
         "#``#",
         "`__`",
        ],

    'I':["`##`",
         "_##_",
         "````",
        ],

    'J':["_`#`",
         "-_#_",
         "```_",
        ],

    'K':["#_-`",
         "#`-_",
         "`__`",
        ],

    'L':["#___",
         "#___",
         "````",
        ],

    'M':["#-_-#",
         "#_`_#",
         "`___`",
        ],

    'N':["#-__#",
         "#_`-#",
         "`___`",
        ],

    'O':["#``#",
         "#__#",
         "````",
        ],

    'P':["#``#",
         "#```",
         "`___",
        ],

    'Q':["-``-",
         "`-#`",
         "__``",
        ],

    'R':["#``#",
         "#`#`",
         "`__`",
        ],

    'S':["#```",
         "```#",
         "````"
        ],

    'T':["`##`",
         "_##_",
         "_``_",
        ],

    'U':["#__#",
         "#__#",
         "````",
        ],

    'V':["#___#",
         "_#_#_",
         "__`__",
        ],

    'W':["#___#",
         "#_-_#",
         "_`_`_",
        ],

    'X':["`-_-`",
         "_-`-_",
         "`___`",
        ],

    'Y':["#__#",
         "`##`",
         "_``_",
        ],

    'Z':["```#`",
         "_-`__",
         "`````",
        ],

    '!':["#",
         "`",
         "`",
        ],

    ' ':["_",
         "_",
         "_",
        ],
}

def letterToBlocks(c):
    """Returns block style of input letter."""
    result = ""
    for i in range(3):
        # result = charToBlock("____") + result
        for ind, j in enumerate(c):
            if ind == 0:
                part = charToBlock("____") + charToBlock(letters[j][i]) + charToBlock('_')
            else:
                part = charToBlock(letters[j][i]) + charToBlock('_')
            result = result + part #+ charToBlock(letters[j][i]) + charToBlock('_')
        result = result + charToBlock("___") + '\n'
        # result = charToBlock("____") + result
    result = '\n' + result
    for i in c:
        spaces = "_" * (len(letters[i][0]) + 1)
        result = result + charToBlock(spaces)
        result = charToBlock(spaces) + result
    result = result + charToBlock("_______")
    result = charToBlock("_______") + result
    return result

def charToBlock(c):
    """Returns char c to block character."""
    result = ""
    for i in c:
        if i == '\n' or i == ' ':
            result = result + i
            continue
        result = result + blocks[i]
    return result
