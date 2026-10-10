# Vector Analysis Logic #

# Q: What is the total area of active parcels? #

SET total = 0 \
FOR each parcel in parcels \
    &emsp;IF parcel is active  \
&emsp;&emsp;ADD parcel area_sqm to total \
&emsp;ENDIF \
ENDFOR \
RETURN total 


