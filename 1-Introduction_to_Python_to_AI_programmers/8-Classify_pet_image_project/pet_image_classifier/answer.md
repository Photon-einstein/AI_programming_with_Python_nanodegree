# Pet image classifier

1. Did the three model architectures classify the breed of dog in Dog_01.jpg to be the same breed?\
   If not, report the differences in the classifications.

   Alexnet: Yes (Beagle)
   resnet: Yes (Beagle)
   vgg: Yes (Beagle)

2. Did each of the three model architectures classify the breed of dog in Dog_01.jpg to be the same\
   breed of dog as that model architecture classified Dog_02.jpg? If not, report the differences\
   in the classifications.

   Alexnet | Dog_01: Beagle, Dog_02: basenji -> No matching classifiers
   resnet | Dog_01: Beagle, Dog_02: "italian greyhound" -> No matching classifiers
   vgg | Dog_01: Beagle, Dog_02: "italian greyhound" -> No matching classifiers

3. Did the three model architectures correctly classify Animal_Name_01.jpg and Object_Name_01.jpg to\
   not be dogs? If not, report the misclassifications.

   Alexnet: Yes
   resnet: Yes
   vgg: Yes

4. Based upon your answers for questions 1. - 3. above, select the model architecture that you feel\
   did the best at classifying the four uploaded images. Describe why you selected that model\
   architecture as the best on uploaded image classification.

   Based on the answers 1 - 3, I cannot select the model that did best, as they obtained similar results.
