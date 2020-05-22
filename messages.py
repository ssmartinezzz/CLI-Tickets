
SV_START = "Server starting...\n"

SV_WAITING = "Server waiting for clients \n"

SV_CONNECTION = ">>Server got connection from"

SV_THREAD = "Initializing thread..\n"

SCKT_ERROR = "Error while creating the socket. Stopping execution"

SCKT_CREATED = "Socket succesfully created!"

SCK_CLOSED = "Socket closed! Client disconected: "

CLIENT_MENU = """-----Operation Menu-----\n
commands available:\n
--insert / -i It allows to create a new ticket. \n
           
--list / -l It allows to list tickets \n
            alternatives: -a(List all the tickets available) -f(allows to introduce filters) \n
            
--edit / -e It allows to edit a ticket with ID \n
                        
            
--exit      Disconnect the client
"""
OPT_ADD_TICK = "Create a new ticket.subcommands: -t{Title} -a{Author} -d{Description}\n"

OPT_LIST_TICK = "You've selected to list ticket/s.\n -v to list all. Pagination aplicable with -p\n Optional filter arguments usage: -a{Author} -d{Date} -s{status} -p{pageN°}\n"

OPT_EDIT_TICK = "You've selected to edit a ticket. subcommands: -i{id} -t{Title} -s{status} -d{Description}\n"

OPT_EXPORT_TICK = "You've selected to export ticket/s.\n"

OPT_EXIT = ">>Shutting down the conection, bye!"

OPT_WRONG = "Invalid option. Press enter to continue..."

ERR_MSG_STATUS = "Invalid status input"

ERR_MSG_INPUT = "Invalid input"

ERR_MSG_NOAVAILABLE = "NOT FOUNDED RESOURCE"

ERR_MSG_NO_DATA = "SERVER COULDN'T RECIEVE DATA FROM CLIENT"

TCKT_FOUND = "TICKET FOUNDED TO MODIFY:"

TCKT_CREATED ="Ticket succesfully created!"

TCKTS_LISTED =">>Send: List of tickets to client: "

CLIENTS_NEWT_CREATED= "A new ticket was created"
