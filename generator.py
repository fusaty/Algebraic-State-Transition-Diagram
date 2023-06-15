import sys

if len(sys.argv) != 2:
    print("Usage: python3 generator.py <input_file>")
    sys.exit(1)
   
input_file_path = sys.argv[1]
   
# define the start words for each line
start_words = ["EventType->", "Image->", "CommandLine->", "TargetFileName->"]

# open the text file for reading
with open(input_file_path, 'r') as f:
    # read in the text from the file and split it into lines
    lines = f.readlines()

# initialize the variables
eventType = ""
image = ""
commandLine = ""
targetFileName = ""

# loop over each line in the file
for line in lines:
    # loop over each start word
    for i, start_word in enumerate(start_words):
        # check if the line contains the start word
        if start_word in line:
            # get the text after the start word and assign it to the appropriate variable
            value = line.split(start_word)[1].strip()
            if i == 0:
                eventType = value
            elif i == 1:
                image = value
            elif i == 2:
                commandLine = value
            else:
                targetFileName = value
            # break out of the inner loop once a start word is found
            break

if not eventType or not image:
    print("Error: Mandatory value is empty.")

# open a new text file for writing
with open('guard1', 'w') as f:
    # write the variables to the new file
    f.write(f"first = \"{image}\"")

if not commandLine and not targetFileName:
    print("Error: Both commandLine and targetFileName are empty.")
elif commandLine:
    # open a new text file for writing
    with open('guard2', 'w') as f:
        # write the variables to the new file
        f.write(f"second = \"{commandLine}\"")

elif targetFileName:
    # open a new text file for writing
    with open('guard2', 'w') as f:
        # write the variables to the new file
        f.write(f"second = \"{targetFileName}\"")



# Define the string to write to the file with the event type variable included
text1 = f"""(attack,
    <aut;
      {{
        (n0->elem),
        (n1->elem),
        (n2->elem)
      }};
      {{
        ((local,n0,n1),a(eventType,_,_,_,_,?first : string), {{file : "guard1"}},"",false),"""

textCMD = f"""\n        ((local,n1,n2),b(?second : string,_,_,_,_,_,_,_), {{file : "guard2"}},"Functions.action1(count, thres)",false)\n"""
textFileName = f"""\n        ((local,n1,n2),b(_,_,_,_,_,_,_,?second : string), {{file : "guard2"}},"Functions.action1(count, thres)",false)\n"""

text2 = f"""      }};
      {{n0,n1,n2}};
      {{}};
      n0
>)
{{
(eventType,string)->{{"{eventType}","{eventType}"}},
(count,int)->[0,4000],
(thres,int)->[0,100]
}};

(MAIN,
     <*;
       imports : {{"functions.ml"}};
       attributes : {{
           (count,int,0),
           (thres,int,1)
       }};
       <|||:;
         (eventType,string);
         {{"{eventType}","{eventType}"}};
         <call;
          attack;
          {{
           eventType->eventType,
           count->count,
           thres->thres
          }}
         >
      >
 >)
 """


# open a new text file for writing spec file
if commandLine:
    with open('attack.spec', 'w') as f:
        # Write the string with the variables to the new file
        f.write(text1+textCMD+text2)

if targetFileName:
    with open('attack.spec', 'w') as f:
        # Write the string with the variables to the new file
        f.write(text1+textFileName+text2)
