# SYNAPSETOOLS   

Simple GUI tools created to help video editors at Synapse in some simple tasks of their post-production workflows without the need of using MacOS's Terminal.   
   
   
Tools available:   
* burnsub: Burns an ass format subtitle into a video file, currently does not deals well with multiple audio channels on ProRes files.   
* dcptovideo: Convert DCP video and audio MFX files to ProRes or H.264 files, currently need improvement when dealing with H.264.   
* contojson: Convert a CSV in a standard model to json for usage with the company specific mongoDB.   
* pplatojson: Same as contojson, different standard model and data.
   
   
   
Installation:   
* git clone git@github.com:gustavohmsilva/synapsetools.git
* pip3 install easygui   
* brew install ffmpeg --enable-ffplay   
* PATH="/Users/Shared/scripts:${PATH}" && export PATH   
* mkdir /Users/Shared/scripts   
* cd synapsetools   
* mv * /Users/Shared/scripts/   
   
   
   
   
Keep in mind that: 

1 - This code was made for use in my company, I do not provide free support for it. In case anyone need a personalized version or any modification and can't do it yourself, please contact-me over e-mail: gus[at]tesserato.video

2 - Giving the scope of the project, All comments, variables and other elements may be in Portuguese, If you don't speak the language, be calm and read the code, it's not rocket science (or hire me for personalizing the source code as your needs).

3 - Any thanks, love letters and dank memes should be send to gustavohmsilva[at]gmail.com or gus[at]tesserato.video

4 - Want to donate something to me? I accept sonic screwdrivers, retrocomputing hardware and [Amazon.com Gift Cards](https://www.gyft.com/buy-gift-cards/amazon-com/).
