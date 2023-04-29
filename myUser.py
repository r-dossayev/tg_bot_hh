

import main

c = main.bot

states = {
    0: [c.message_handler(func=main.selectCateg,)],
    1: [c.message_handler(func=main.newJobVacs)],
    2: [c.message_handler(func=main.newJobInputs)],

}
