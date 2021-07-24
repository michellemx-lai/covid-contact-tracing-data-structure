# CovidData

Built with Python, this data structure is used to acess, analyze, and manipulate a set of fictitious COVID-19 contract tracing data.

I was provided a (fictitious) dataset of information collected by a COVID-19 contact tracer, and I developed data structures that allow quick access to and manipulation of that data. 

Completed in the middle of the COVID-19 pandemic, this project gave me a sense of the power of coding to gather and display data, and help in understanding important worldwide events. 

# The Code

This project is separated into five parts: 

Part 1 – Represent the Contact Tracing Data
    I designed and implemented a data structure that will be used to represent information about an infected person, and others infected by contact with that person.

Part 2 – Parse the Contract Tracing Data
    I designed and implemented a function to process the content of a file containing data on persons and infections. The data file is in csv format and has the following structure:

    id,infected-by,date a3959d249c3444dbb36310bb16e2a689,d03ba6ffa3b5475989ce477973d1617d,2021-02-09 ae66eefa796a4a59aa375d0514620fcf,209864c2f0f543089f8466e7bcff3acd,2021-01-27 435e781627db4635b966c3d4fd493728,d161fa8d17f244d186ef9a47b40e931c,2021-03-21 0583968bf83442858853ef7c2d0f75cb,c921ae9021ab440aa440601e20fdb45f,2021-01-16

Part 3 – Identify the Top Direct Superspreaders
    A “direct superspreader” is a person who directly infects many others. In this part, I designed and implemented a function to identify the top direct superspreader(s): the person(s) that directly infected the most other persons.

Part 4 – Find Superspreading Dates
    We define a superspreading date as the date in which the most persons were infected. Ties are possible and so there may be multiple direct superspreading dates. In this part, the superspreading dates are identified and extracted. 

Part 5 – Identify the Top (Direct + Indirect) Superspreaders
    In Part 3 I looked at direct infections: when one person infects one or more others. Indirect infections are the ones that follow from a direct infection. For example, if person A infects person B and person B infects persons C and D, A is said to have indirectly infected C and D. If C and D do not infect anyone else, A is said to have (directly + indirectly) infected three persons: B, C, and D. In this part, I designed and implemented two functions to identify all people directly or indirectly infected by a person, and to identify the top (direct + indirect) superspreader(s).
