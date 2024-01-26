# Disk Imaging

A forensic image is an electronic copy of a drive (e.g. a hard drive, USB, etc.). It’s a bit-by-­bit or bitstream file that’s an exact, unaltered copy of the media being duplicated.

Wikipedia said that the most straight­forward disk imaging method is to read a disk from start to finish and write the data to a forensics image format. “This can be a time-consuming process, especially for disks with a large capacity,” Wikipedia said.

To prevent write access to the disk, you can use a write blocker. It’s also common to calculate a cryptographic hash of the entire disk when imaging it. “Commonly-used cryptographic hashes are MD5, SHA1 and/or SHA256,” said Wikipedia. “By recalculating the integrity hash at a later time, one can determine if the data in the disk image has been changed. This by itself provides no protection against intentional tampering, but it can indicate that the data was altered, e.g. due to corruption.”

Why image a disk? Forensic imaging:
- Prevents tampering with the original data­ evidence
- Allows you to play around with the copy, without worrying about messing up the original

## Forensic Image Extraction Exmple

This example uses the tool [AccessData FTK Imager](http://accessdata.com/product-download).

**Step 1**: Go to `File > Create Disk Image`

![File Image Demo](images/image-demo-1.png)

**Step 2**: Select `Physical Drive`, because the USB or hard drive you’re imaging is a physical device or drive.

![File Image Demo](images/image-demo-2.png)

**Step 3**: Select the drive you’re imaging. The 1000 GB is my computer hard drive; the 128 MB is the USB that I want to image.

![File Image Demo](images/image-demo-3.png)

**Step 4**: Add a new image destination

![File Image Demo](images/image-demo-4.png)

**Step 5**: Select whichever image type you want. Choose `Raw (dd)` if you’re a beginner, since it’s the most common type

![File Image Demo](images/image-demo-5.png)

**Step 6**: Fill in all the evidence information

![File Image Demo](images/image-demo-6.png)

**Step 7**: Choose where you want to store it

![File Image Demo](images/image-demo-7.png)

**Step 8**: The image destination has been added. Now you can start the image extraction

![File Image Demo](images/image-demo-8.png)

**Step 9**: Wait for the image to be extracted

![File Image Demo](images/image-demo-9.png)

**Step 10**: This is the completed extraction

![File Image Demo](images/image-demo-10.png)

**Step 11**: Add the image you just created so that you can view it

![File Image Demo](images/image-demo-11.png)

**Step 12**: This time, choose image file, since that’s what you just created

![File Image Demo](images/image-demo-12.png)

**Step 13**: Enter the path of the image you just created

![File Image Demo](images/image-demo-13.png)

**Step 14**: View the image.

1. Evidence tree
Structure of the drive image
2. File list
List of all the files in the drive image folder
3. Properties
Properties of the file/folder being examined
4. Hex viewer
View of the drive/folders/files in hexadecimal

![File Image Demo](images/image-demo-14.png)

**Step 15**: To view files in the USB, go to `Partition 1 > [USB name] > [root]` in the Evidence Tree and look in the File List

![File Image Demo](images/image-demo-15.png)

**Step 16**: Selecting fileA, fileB, fileC, or fileD gives us some properties of the files & a preview of each photo

![File Image Demo](images/image-demo-16.png)

**Step 17**: Extract files of interest for further analysis by selecting, right-clicking and choosing `Export Files`

![File Image Demo](images/image-demo-17.png)