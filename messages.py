"""
This python file contains all the messages or strings that are shown in
client terminals as well as server's terminal.
"""

SV_START = "Server starting...\n"

SV_WAITING = "Server waiting for clients \n"

SV_CONNECTION = ">>Server got connection from"

SV_RECV_ID = ">>Server recieved Id: "

NEW_PROCESS = ">>Exporting a ticket. Client: "

SV_THREAD = "Initializing thread 'ID':"

SCKT_ERROR = "Error during creating the socket. Stopping execution"

SCKT_CREATED = "Socket succesfully created!"

SCK_CLOSED = "Socket closed! Client disconected: "

CLIENT_MENU = """-----Operation Menu-----\n
commands available:\n
--insert / -i It allows to create a new ticket. \n
           
--list / -l It allows to list tickets \n
            
--edit / -e It allows to edit a ticket with ID \n

--export / -x It allows to export tickets to a csv file
                        
--clear / -c You can clear the terminal            
--exit      Disconnect the client
"""
OPT_ADD_TICK = "Create a new ticket.subcommands: -t{Title} -a{Author} -d{Description}\n"

OPT_LIST_TICK = "You've selected to list ticket/s.\n " \
                "-v to list all. Pagination aplicable with -p" \
                "\n Optional filter arguments usage: -a{Author} -d{Date} -s{status} -p{pageN°}\n"

OPT_EDIT_TICK = "You've selected to edit a ticket. subcommands: -i{id} -t{Title} -s{status} -d{Description}\n"

OPT_EXPORT_TICK = "You've selected to export ticket/s.\n -v to export all tickets " \
                  "\nOptional filter arguments usage: -a{Author} -d{Date} -s{status}\n" \
                  "Pagination aplicable with -p\n"

OPT_EXIT = ">>Shutting down the conection, bye!"

OPT_WRONG = "Invalid option. Press enter to continue..."

ERR_MSG_STATUS = "Invalid status input"

ERR_MSG_INPUT = "Invalid input"

ERR_MSG_DATE = "Invalid date input"

ERR_MSG_NOAVAILABLE = "NOT FOUNDED RESOURCE"

ERR_MSG_COULDNT = "SERVER COULDN'T RECIEVE DATA FROM CLIENT"

ERR_MSG_BP = "Broken pipe!"

TCKT_FOUND = "TICKET FOUNDED TO MODIFY:"

TCKT_EDITED = ">>Ticket Edited by"

TCKT_CREATED ="Ticket succesfully created!"

TCKT_BRD = "A client created a ticket"

TCKTS_LISTED =">>Send: List of tickets to client: "

CLIENTS_NEWT_CREATED= "A new ticket was created"

CLIENT_EXPORT_SUCCESS= "Tickets exported in your directory"

CLIENT_CLEARED = "A client cleared its own terminal"

KYBRD_INTERRUPT = "Keyboard interrupted"

EOFE = "¡EOFE!"
