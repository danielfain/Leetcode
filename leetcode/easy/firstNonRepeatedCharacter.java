public static Character firstNonRepeatedCharacter(String str) {

    HashMap<Character, Integer> hm = new HashMap<>();

    for (int i = 0; i < str.length(); i++) {
        char letter = str.toCharArray()[i];

        if (hm.containsKey(letter)) {
            int count = hm.get(letter);
            hm.put(letter, count + 1);
        } else {
            hm.put(letter, 1);
        }
    }

    for (int i = 0; i < str.length(); i++) {
        int result = hm.get(str.toCharArray()[i]);
        if (result == 1) {
            return str.toCharArray()[i];
        }
    }

    return null;
}