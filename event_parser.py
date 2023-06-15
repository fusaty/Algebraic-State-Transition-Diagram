import json
import os
import pprint

_dir = 'data/'

fout = open('audit_events.log', 'w') 

for fn in os.listdir(_dir):
   with open(_dir+fn) as afile:
      #load json object 
      #data = json.load(f)
      event='""'
      systime = '""'
      image = '""'
      cmdline = '""'
      pid = '""'
      targetobject = '""'
      targetfilename = '""'
      details = '""'
      hashes = '""'
      proto = '""'
      addr_src = '""'
      port_src = '""'
      addr_dst = '""'
      port_dst = '""'

      for line in afile:
     
         if '}' in line: 
           event_astd = 'a('+event+','+systime+','+ port_dst+','+pid+','+targetobject+','+image+ ')' + '\n' +  'b(' + cmdline+','+details+','+hashes+','+proto+','+addr_src+','+port_src+','+addr_dst+','+targetfilename+')' + '\n'
           fout.write(event_astd+'\n') 
         else:    
            # feature extraction
            data = line.strip()
            tmp_ = data.split(': ')

            if 'System.EventID.text' in data:
               tmp = tmp_[1]
               if '1' in tmp:
                   event = '"Process creation"'
               if '2' in tmp:
                   event = '"A process changed a file creation time"'
               if '3' in tmp:
                   event = '"Network connection"'
               if '4' in tmp:
                   event = '"Sysmon service state changed"'
               if '5' in tmp:
                   event = '"Process terminated"'
               if '6' in tmp:
                   event = '"Driver loaded"'
               if '7' in tmp:
                   event = '"Image loaded"'
               if '8' in tmp:
                   event = '"Create Remote Thread"'
               if '9' in tmp:
                   event = '"Raw Access Read"'
               if '10' in tmp:
                   event = '"Process Access"'
               if '11' in tmp:
                   event = '"File Create"'
               if '12' in tmp:
                   event = '"Registry Event Create and Delete"'
               if '13' in tmp:
                   event = '"Registry Event Set"'
               if '14' in tmp:
                   event = '"Registry Event Rename"'
               if '15' in tmp:
                   event = '"File Create Stream Hash"'
               if '17' in tmp:
                   event = '"Pipe Created"'
               if '18' in tmp:
                   event = '"Pipe Connected"'
               if '19' in tmp:
                   event = '"WMI Event Filter activity detected"'
               if '20' in tmp:
                   event = '"WMI Event Consumer activity detected"'
               if '21' in tmp:
                   event = '"WMI Event Consumer To Filter activity detected"'
               if '23' in tmp:
                   event = '"File Delete"'
               if '255' in tmp:
                   event = '"Sysmon Error"'

            if 'System.TimeCreated.SystemTime' in data:
               systime = tmp_[1].rstrip(',') 
            if 'EventData.Data.Image' in data:
               image = tmp_[1].rstrip(',') 
               if '\\\\' in image:
                    pom = image.replace('\\\\', "/")
                    image = '"' + pom + '"' 
               if '"' in image:
                    pom = image.replace('"', "")
                    image = '"' + pom + '"' 
            if 'EventData.Data.CommandLine' in data:
               cmdline = tmp_[1].rstrip(',')
               if '\\\\' in cmdline:
                    pom = cmdline.replace('\\\\', "/")
                    cmdline = '"' + pom + '"' 
               if '"' in cmdline:
                    pom = cmdline.replace('"', "")
                    cmdline = '"' + pom + '"' 
            if 'EventData.Data.ProcessId' in data:
               pid = tmp_[1].rstrip(',')
            if 'EventData.Data.TargetObject' in data:
               targetobject = tmp_[1].rstrip(',')
            if 'EventData.Data.TargetFilename' in data:
               targetfilename = tmp_[1].rstrip(',')
               if '\\\\' in targetfilename:
                    pom = targetfilename.replace('\\\\', "/")
                    targetfilename = '"' + pom + '"' 
               if '"' in targetfilename:
                    pom = targetfilename.replace('"', "")
                    targetfilename = '"' + pom + '"' 
            if 'EventData.Data.Details' in data:
               details = tmp_[1].rstrip(',')
            if 'EventData.Data.Hashes' in data:
               hashes = tmp_[1].rstrip(',')
            if 'EventData.Data.Protocol' in data:
               proto = tmp_[1].rstrip(',')
            if 'EventData.Data.SourceIp' in data:
               addr_src = tmp_[1].rstrip(',')
            if '"EventData.Data.SourcePort"' in data:
               port_src = tmp_[1].rstrip(',')
            if 'EventData.Data.DestinationIp' in data:
               addr_dst = tmp_[1].rstrip(',')
            if '"EventData.Data.DestinationPort"' in data:
               port_dst = tmp_[1].rstrip(',')

fout.close() 
 

       
