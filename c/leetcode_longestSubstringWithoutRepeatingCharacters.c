int lengthOfLongestSubstring(char* s) {
    int index=0, last=0, i;
    int max = 0, new_max = 0;
    while (*(s+index) != '\0') {
        for (i=last; i<index; i++) {
            if (*(s+i) == *(s+index)) break;
        }
        if (i != index) {
            new_max = index - last;
            max = (new_max>max) ? new_max : max;
            last = i + 1;
        }
        index += 1;
    }
    new_max = index - last;
    max = (new_max>max) ? new_max : max;
    return max;
}
