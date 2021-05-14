# JSONonense
A generator for creating arbitrary JSON objects from various sources.

## Configured values
##### MIN_KEY_PER_OBJECT | MAX_KEY_PER_OBJECT
The minimum and maximum number of keys per object.

##### MAX_DEPTH
The maximum depth generated. Maximum allowed is 20 until optimization.

##### OBJ_CHANCE
The percent chance for a generated value to be an obj instead of a literal.
    
## Default Generation
Generates objects with string, integer, float, and null values, with a max depth of 5.