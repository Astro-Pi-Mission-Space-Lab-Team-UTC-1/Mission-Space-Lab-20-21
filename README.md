# Astro Pi | Mission Space Lab | UTCR

### Imported Packages
- [pillow](https://pillow.readthedocs.io/en/stable/index.html "Python Imaging Library")
- [ephem](https://pypi.org/project/ephem/ "High Precision Astronomy Computations")
- [picamera](https://picamera.readthedocs.io/en/release-1.13/index.html "Raspberry Pi camera module")


### Brief Description
The main.py file will run for approximately 3 hours.

The algorithm writes data to csv after every 10 images taken.

Below is a simplified flowchart of the program.

- **RF** - Raw Folder
- **PF** - Processed Folder

[![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggTFIgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIFxuICAgIEEoW1N0YXJ0XSkgLS0-IEJbQ3JlYXRlIHN0YXJ0dXAgZm9sZGVyc10gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgXG4gICAgQiAtLT4gQ3szIGhvdXJzIHBhc3NlZD99ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBcbiAgICBDIC0tPiB8WWVzfCBEW1t3cml0ZSBjc3ZdXSAtLT4gWihbRW5kXSkgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIFxuICAgIEMgLS0-IHxOb3wgRVt0YWtlIHBpY3R1cmUgYWZ0ZXIgNSBzZWNvbmRzXSAtLT4gRltTYXZlIHBpY3R1cmUgdG8gUkYgZm9sZGVyXSAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgXG4gICAgRiAtLT4gR3tJcyAxMCBpbWFnZXMgaW4gUkY_fSAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBcbiAgICBHIC0tPiB8WWVzfCBIW1t3cml0ZSBjc3ZdXSAtLT4gQyAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIFxuICAgIEcgLS0-IHxOb3wgQyIsIm1lcm1haWQiOnsidGhlbWUiOiJkZWZhdWx0In0sInVwZGF0ZUVkaXRvciI6ZmFsc2V9)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoiZ3JhcGggTFIgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIFxuICAgIEEoW1N0YXJ0XSkgLS0-IEJbQ3JlYXRlIHN0YXJ0dXAgZm9sZGVyc10gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgXG4gICAgQiAtLT4gQ3szIGhvdXJzIHBhc3NlZD99ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBcbiAgICBDIC0tPiB8WWVzfCBEW1t3cml0ZSBjc3ZdXSAtLT4gWihbRW5kXSkgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIFxuICAgIEMgLS0-IHxOb3wgRVt0YWtlIHBpY3R1cmUgYWZ0ZXIgNSBzZWNvbmRzXSAtLT4gRltTYXZlIHBpY3R1cmUgdG8gUkYgZm9sZGVyXSAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgXG4gICAgRiAtLT4gR3tJcyAxMCBpbWFnZXMgaW4gUkY_fSAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBcbiAgICBHIC0tPiB8WWVzfCBIW1t3cml0ZSBjc3ZdXSAtLT4gQyAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIFxuICAgIEcgLS0-IHxOb3wgQyIsIm1lcm1haWQiOnsidGhlbWUiOiJkZWZhdWx0In0sInVwZGF0ZUVkaXRvciI6ZmFsc2V9)

[![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggTFIgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIFxuICAgIEFbW3dyaXRlIGNzdl1dIC0tPiBCW09wZW4gY3N2IGZpbGVdICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgXG4gICAgQiAtLT4gQ1tHZXQgZmlsZW5hbWUsIGxhdGl0dWRlLCBsb25naXR1ZGUgLi4uXSAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBcbiAgICBDIC0tPiBEW01vdmUgdG8gUEZdICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIFxuICAgIEQgLS0-IEVbQXBwZW5kIGRhdGEgdG8gZmlsZV0gIiwibWVybWFpZCI6eyJ0aGVtZSI6ImRlZmF1bHQifSwidXBkYXRlRWRpdG9yIjpmYWxzZX0)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoiZ3JhcGggTFIgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIFxuICAgIEFbW3dyaXRlIGNzdl1dIC0tPiBCW09wZW4gY3N2IGZpbGVdICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgXG4gICAgQiAtLT4gQ1tHZXQgZmlsZW5hbWUsIGxhdGl0dWRlLCBsb25naXR1ZGUgLi4uXSAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBcbiAgICBDIC0tPiBEW01vdmUgdG8gUEZdICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIFxuICAgIEQgLS0-IEVbQXBwZW5kIGRhdGEgdG8gZmlsZV0gIiwibWVybWFpZCI6eyJ0aGVtZSI6ImRlZmF1bHQifSwidXBkYXRlRWRpdG9yIjpmYWxzZX0)


### Detailed breakdown

**RF & PF**

One of our first concerns was whether we should move (copy & paste) files
when they have been processed or rename them. However, according to the
`shutil` docs, `shutil.move()` will rename the file if it is on the the
same file system. [shutil docs](https://docs.python.org/3/library/shutil.html#shutil.move)

> Having 2 folders allows us to easily manage which files need to be processed.


**Numbering Conventions**

The numbering convetion for the cloud images goes as such:

> *cloud_1.jpg, cloud_2.jpg, cloud_3.jpg ... *

Since there is only 1 csv file used in the program it is called *data01.csv*


**Lat/Long Format**

We decided to write the calculated longitude and latitude data in **decimal** form,
rather than `degrees:minutes:seconds`, since it is what we are more familiar with.


**Cloud Coverage**

We collected the cloud coverage data in 2 units. The first was as a percentage and the second
in oktas. Oktas are a way of measuring cloud coverage by dividing the visible are into 8 boxes
and how many of those boxes the visible clouds take up.

By taking the readings in oktas it makes it easier for us to interpret the data/image and
identify anomolies during testing. Which lead us to adjust our image processing algorithm.
This data can also be used when reviewing the data in phase 4.


**Image Processing**

![](https://live.staticflickr.com/4880/46142459702_68601f4372_w_d.jpg)

*Image from https://flic.kr/p/2disaG*

As shown in the image above from a previous Astro Pi Mission, there is a black ring.
To calculate an accurate percentage of clouds we created a filter that will keep track
of the number of dark pixels. We also created a filter that will count the number of
'cloud' pixels.

&nbsp;

$total\ usuable\ pixels = total\ pixels\ -\ dark\ pixels$

$percentage\ of\ clouds = \frac{clouds\ pixels}{total\ usable\ pixels} \times 100$

&nbsp;

Each pixel has a red, green and blue value which each has a max size of 255.
The lowest possible out put for the sum of these values is 0 and the greatest is 765.
Where 0 is black and 765 is white. By repeating this process for every pixel and defining
thresholds which identify as the pixel as 'dark', 'cloud' or neither, we used it as a filter.

By increasing the contrast before processing the image we managed to distinguish the 'dark'
and 'cloud' pixels better, increasing the precision of the algorithm.

**Storage Management**

The amount of storage for the program to run is 3GB or 3,072MB.
The program is running for 3 hours or 10,800 seconds.
An image is taken every 5 seconds.

&nbsp;

$\therefore average\ image\ file\ size = \frac{3,072}{\frac{10,800}{5}}$

$\therefore average\ image\ file\ size = 1.42MB$

&nbsp;

The average file size during testing was **1MB**

The python files take **less than 0.5MB**

&nbsp;

Assuming averge image file size is 1MB

$total\ image\ storage = 1 \times \frac{3 \times 60 \times 60}{5} = 2,160MB$

$total\ free\ space = 3,072 - 2,160 = 912MB$

&nbsp;

This is more than enough storage for the csv file and python files.
For this reason we are have not deleted the images so we can review them in phase 4.


### Contributors

Samson Nagamani <samson.nagamani@pm.me>
Sam Quail <sam@squail.org>
Sonia Kumar <sonia.kumar.242@gmail.com>
Matt Nock <thematt.nock@gmail.com>
