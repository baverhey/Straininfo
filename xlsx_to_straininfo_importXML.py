#! /usr/bin/python
# This program Converts a DB dump of an BRC collection to the XML straininfo upload format 
# 
# #INPUT
#   DB dump file of brc in csv 
#	
#   Source file with 1 colum per db field
#   
#   OPTIONS
#    -c --csv_delimiter_input   Defines the delimiter value of the source file, default is set to ;
#    -d --debug        debug information progres and messages
#    -v --verbose  verbose progres and messages
#
# usage: map_BRC_alias_to_genomes.py [options ] <inputfilein csv> <inputfilein csv> <int>
# syntax: python3 map_BRC_alias_to_genomes.py -c ';' --header -v -d LMG_alias.csv gold_genomes.csv 15
# python3 map_BRC_alias_to_genomes.py -c ';' -C ';' --header LMG_alias.csv gold_genomes.csv 15 > LMG_genome_result_list.csv 2>genomen_niet_in_LMG.csv




#@todo
#compleet translation to english
#Sensible use of the -v verbose messaging
#More readable debug output -d
#sensable output to error stream when something is wrong
#extra output form if nessesairy
#Better help texts

__author__="baverhey"
__date__ ="$10-februari-2014 14:31:47$"


import argparse # needed for reading the options 
import os   #needed for file and directory manipulations
import pprint   #needed for pretty print nicer output for debug
import sys #for writing to strr


def processcommandline():
    
    desc="""
    Processes all the comand line options, validates and stores the flags ready for use
    """
    # Makes variable options anywhere available

    global args
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', action='version', version='%(prog)s version 0.1')
    parser.add_argument("-c", "--csv_delimiter_input",
                       action="store",
                       nargs='?',
                       dest="o_csv_delimiter_input_value",
                       default=";",
                      help="Defines the delimiter value of the source files, default is set to ;")
                                           
    parser.add_argument("-C", "--csv_delimiter_output",
                       action="store",
                       nargs='?',
                       dest="o_csv_delimiter_output_value",
                       default="\t",
                      help="Defines the delimiter value of the output, default is set to \t")
                      
    parser.add_argument("-d", "--debug",
                      action="store_true",
                      dest="o_debug_flag",
                      default=False,
                      help="Writes all kinds of debug info, step by step, and progres not good for piping")

    parser.add_argument("--header",
                      action="store_true",
                      dest="o_header_flag",
                      default=False,
                      help="When the header flag is set the first line of the input file will be skipped and used for dynamic mapping to the xml labels. default false standard order of xml ")
    
    parser.add_argument("-v", "--verbose",
                      action="store_true",
                      dest="o_verbose_flag",
                      default=False,
                      help="Writes all kinds of info for folowing progress, not good for piping")

    parser.add_argument("-p", "--processors",
                      action="store",
                      nargs='?',
                      dest="o_processors_value",
                      type=int,
                      default=1,
                      help="Number of processors / cores available default 1")

    #positional arguments                  
    parser.add_argument('brc_dump_sourcefile',
                      help= "The file that contains the BRC database fields"
                        

    args = parser.parse_args()
    
   
        
    #helper flag for sending csf header to print
    args.o_header_sent=False
            
    # flags are filled and processed (arguments in correct file extension?)
    #test 1 file

    #done processing commandline

	
	
def read_input_file_BRC_DB_dump(input_file):	
	
	'''
	Here the input file is read line by line, the lines are split in the correct ditionarys
	When the file is correct ly split the line is processed by different function.
	This way in the futer we can have multiple input file types but the same xml generation functions for the prcessed lines
	'''
	
	#If there is a header line/block
		#read as long we are in the header block with the collection information
		dict_header =split_input_line_colectioninfo_to_dict(header_block)
		xml_header_brc_info = xml_generate_header(dict_header)
		#write to standard out
	#else
		#for eats folowing line that is aculture
			dict_culture = split_input_line_culture_to_dict(line_culture)
			xml_culture=xml_process_culture(dict_culture)
			#Write to standard out
			
	#dont forget to close the nesesairy levels for valid xml
	#done processing input file		
	
	None
	
	
def xml_generate_header(dict_BRC_information):	
	
	'''
	Here the dictionary contains all nesesairy fields to generate the STRAININFO.net XML:MCL header
	The XML header is generated
	
		<mcl:Catalog xmlns:mcl="http://www.straininfo.net/ns/mcl/2.0/"
          xmlns:dc="http://purl.org/dc/elements/1.1/"
          xmlns:dcterms="http://purl.org/dc/terms/"
          xmlns:prism="http://prismstandard.org/namespaces/basic/2.0"
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xsi:schemaLocation="http://www.straininfo.net/mcl/2.0/ http://www.straininfo.net/schema/2.0/si-catalog.xsd">

			<mcl:CatalogDescription>
				<dc:creator>Bert Verslyppe</dc:creator>
				<dcterms:created>2010-01-01T09:05:37</dcterms:created>
				
				<mcl:catalogVersion>v9.2b 20091231</mcl:catalogVersion>
				<mcl:catalogLastUpdateDate>2009-12-31T13:30:00</mcl:catalogLastUpdateDate>
				
				<mcl:BRC>
					<mcl:WDCMNumber>1024</mcl:WDCMNumber>
					<mcl:fullName>StrainInfo Demo Collection</mcl:fullName>
					<mcl:acronym>SD</mcl:acronym>
				</mcl:BRC>
			</mcl:CatalogDescription>
	'''
	
	None
	return xml_header_brc_info

def xml_process_culture(dict_culture_information):	
	
	'''
	Here the dictionary contains all nesesairy fields to generate the STRAININFO.net XML:MCL culture data block
	The XML culture is generated
	
	<mcl:Culture>
		<mcl:strainNumber>LMG 24056</mcl:strainNumber>
		<mcl:otherStrainNumber>DSM 44871</mcl:otherStrainNumber>
		<mcl:otherStrainNumber>Trujillo LUPAC 09</mcl:otherStrainNumber>
		<mcl:catalogURL>http://bccm.belspo.be/db/lmg_strain_details.php?NUM=24056</mcl:catalogURL>
		<mcl:cultureLastUpdateDate>2008-08-05T12:30:00</mcl:cultureLastUpdateDate>
		
		<mcl:speciesName>Micromonospora saelicesensis</mcl:speciesName>
		<mcl:nomenclaturalPublication>
			<dcterms:bibliographicCitation>Trujillo, Kroppenstedt, Fernandez-Molinero, Schumann and Martinez-Molina 2007</dcterms:bibliographicCitation>
		</mcl:nomenclaturalPublication>      
		
		<mcl:isolationDate>2003</mcl:isolationDate>
		<mcl:isolator>M.Trujillo</mcl:isolator>
		<mcl:isolatorInstitute>Dep. de Microbiologia y Genetica Universidad de Salamanca</mcl:isolatorInstitute>
		<mcl:Sample>
			<mcl:sampleLocationCountry>Spain</mcl:sampleLocationCountry>
			<mcl:sampleLocationPlace>Salamanca</mcl:sampleLocationPlace>
			<mcl:sampleHabitat>Lupinus angustifolius, root nodule</mcl:sampleHabitat>
		</mcl:Sample>
		<mcl:Deposit>
			<mcl:resultingStrainNumber>LMG 24056</mcl:resultingStrainNumber>
			<mcl:depositDate>2007</mcl:depositDate>
			<mcl:depositor>M.Trujillo</mcl:depositor>
			<mcl:depositorInstitute>Dep. de Microbiologia y Genetica Universidad de Salamanca</mcl:depositorInstitute>
		</mcl:Deposit>
		<mcl:history>&lt;- 2007, M.Trujillo Dep. de Microbiologia y Genetica Universidad de Salamanca Spain (2003)</mcl:history>
	   
		<mcl:Medium>
			<mcl:mediumNumber>LMG Medium 185</mcl:mediumNumber>
			<mcl:mediumName>Bacteria Culture Medium 185</mcl:mediumName>
			<mcl:mediumURL>http://bccm.belspo.be/db/media_search_results.php?COLL=LMG&amp;FIELD=NUM&amp;TEXT1=185</mcl:mediumURL>
		</mcl:Medium>
		<mcl:growthTemperature>28</mcl:growthTemperature>
	</mcl:Culture>
	'''
	None
	return xml_culture_entry

def xml_process_publication(dict_publication_information):	
	
	'''
	Here the dictionary contains all nesesairy fields to generate the STRAININFO.net XML:MCL publication data block
	The XML culture is generated
	
	<mcl:Publication id="1000">
		<dcterms:bibliographicCitation>Nakamura, L K, Blumenstock, I, Claus, D, Taxonomic study of Bacillus coagulans Hammer 1915 with a proposal for Bacillus smithii sp. nov, Int J Syst Bacteriol, 38, 63-73, 1988</dcterms:bibliographicCitation>
		<dc:title>Taxonomic study of Bacillus coagulans Hammer 1915 with a proposal for Bacillus smithii sp. nov</dc:title>
		<dc:creator>Nakamura, L K</dc:creator>
		<dc:creator>Blumenstock, I</dc:creator>
		<dc:creator>Claus, D</dc:creator>
		<prism:publicationName>Int J Syst Bacteriol</prism:publicationName>
		<prism:number>38</prism:number>
		<prism:pageRange>63-73</prism:pageRange>
		<dcterms:issued>1988</dcterms:issued>
	</mcl:Publication>
	
	'''
	None
	return xml_culture_entry



def split_input_line_culture_to_dict(input_line):	
	
	'''
	Here 1 line of the input file that is a culter is beeing split in the apropriot dictionary with key value pairs
	
	This way a file can be handeld that contains the collection info and the culter info in 1 file	'''
	None
	return dict_culture_information
	
def split_input_line_publication_to_dict(input_line):	
	
	'''
	Here 1 line of the input file that is a publication is beeing split in the apropriot dictionary with key value pairs
	
	This way a file can be handeld that contains the collection info and the culter info in 1 file	'''
	None
	return dict_publication_information
	
	
def split_input_line_colectioninfo_to_dict(input_line):	
	
	'''
	Here 1 or multiple line of the input file(header) that is a colection information is beeing split in the apropriot dictionary with key value pairs
	This way a file can be handeld that contains the collection info and the cultur info in 1 file	'''
	None
	return dict_BRC_information	



	

if __name__ == "__main__":
    
    processcommandline()
	read_input_file_BRC_DB_dump(args.brc_dump_sourcefile)
	
	
	
###For illustration and example	

def read_input_file_BRC_aliases(input_file):

    '''
    Read 1 input file to hashmap
    Read on every line first the brc code and the aliases
    split the aliases on ,
    make hashmap  hmap[alias]=BRC_code
    '''

    #Hashmap
    dict_hmap= {}


    #open file
    with open(input_file, 'r') as filereader :
        #read all lines
        
        # option for skipping header line of input file
        #if options.o_xxxxx_flag :
        #   next( filereader)
        
        linenr=0
        
        for line in filereader:
            
            if args.o_verbose_flag and linenr % 100 == 0 :
                print("Processing line: " , linenr)
                            
            if args.o_debug_flag :
                #print("Input line to process:\n " , line)
                None
    
            #process 1 line
            #clean up line
            
            #remove \n end lines
            line = line.replace('\n','')
            
            
            #split line in 2 fields
            #BRC_code;BRC_aliases
            (brc_code,nr_of_aliases,brc_aliases) = line.split(args.o_csv_delimiter_input_value)

            if args.o_debug_flag :
                #print("Split BRC_code: "+ brc_code +"\n-> aliases: ",brc_aliases)
                None

            #spit the aliasses only
            list_brc_aliases=brc_aliases.split(',')
            
            #save the aliases in the hashmap
            
            for a in list_brc_aliases:
                dict_hmap[a]=brc_code
                
                #if args.o_debug_flag :
                    #print("#####HASH map until now: ")
                    #pp = pprint.PrettyPrinter(indent=4)
                    #pp.pprint(dict_hmap)
                    
            
            linenr= linenr+1
        #end for reading dile

    #close file
    filereader.closed
  
    if args.o_debug_flag :
        print("##Compleet hashmap:  done")
        #print("##Compleet hashmap:  ", dict_hmap)

    #cleanup hashmap not all lines hava brc key
    del dict_hmap['']

    return dict_hmap
   


def read_input_file_compleet_genomes_list(input_file,dict_hmap_aliases):

    '''
    Read 1 input file line by line look in the BRC-code colum 
    and look in the hashmap if found write compleet line
    Read line
    split line by csv sepperator
    get value of brc colum
    look in hashmap
    print BRC collection code, retrieved alias, compleet line to ceep all information
    print to standart out for piping to file
    '''

    #open file
    with open(input_file, 'r') as filereader :
        #read all lines
        
        # option for skipping header line of input file
        #if args.o_header_flag :
           #next( filereader)
           
        #first line is header line
        headerline_genome_sourcefile=next(filereader)
        headerline_genome_sourcefile =headerline_genome_sourcefile.replace('\n','')
        if args.o_debug_flag :
            print("\n##Header line genomesourcefile \n: %s" , headerline_genome_sourcefile)
        
        
        #print the output header
        if not args.o_header_sent and args.o_header_flag :
            #print column header of csv
            kolom_header= "{0}{3}{1}{3}{2}{3}{4}".format("BRC-Code","BRC-code found","data",args.o_csv_delimiter_output_value,headerline_genome_sourcefile)
            print (kolom_header)
            args.o_header_sent=True   
            
        linenr=0
        
        for line in filereader:
            
            if args.o_verbose_flag and linenr % 100 == 0 :
                print("Search genome:   Processing line " , linenr)
            
            if args.o_debug_flag :
                print("Input line to process: " , line)
                
    
            #process 1 line
            #clean up line
            #remove \n end lines
            line = line.replace('\n','')
                       
            #split line in x fields
            
            list_line_fields = line.split(args.o_csv_delimiter_input_value)

            if args.o_debug_flag :
                #print("Splitted fields genome input file: \n" , list_line_fields)
                None

            brc_code_in_genome_inputfile=list_line_fields[args.columnr_BRC_code]
            
            if brc_code_in_genome_inputfile in dict_hmap_aliases:
                if args.o_debug_flag :
                    print("####Found " + brc_code_in_genome_inputfile + " in hashmap")
             
                #the key is in the hashmap compleet genome found
                line_to_print= "{0}{3}{1}{3}{2}".format(dict_hmap_aliases[brc_code_in_genome_inputfile],brc_code_in_genome_inputfile,line,args.o_csv_delimiter_output_value)
                print (line_to_print)
                
            else:
                # the key is not found int he alias list, this collection has not the material
                error_line = "{0}{3}{1}{3}{2}\n".format("BRC-code NOT found in ALIAS HASHMAP",brc_code_in_genome_inputfile,line,args.o_csv_delimiter_output_value)
                sys.stderr.writelines (error_line)
            
            linenr=linenr +1
        #end for reading file

    #close file
    filereader.closed
  


    