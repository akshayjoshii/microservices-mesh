import string

class PasswordStrengthChecker:
    def __init__(self, password):
        
        self.password = password
        self.password_length = len(password)

    def letters_only_score(self):
        letter_count = self.count_char_type(string.ascii_lowercase + string.ascii_uppercase)
        
        # If all the chars in the password are just letters, then penalize by the 
        # factor of length of the password
        if self.password_length == letter_count:
            return - 1 * self.password_length
        
        # Else do not penalize (show mercy)
        return 0
    
    def numbers_only_score(self):
        digit_count = self.count_char_type(string.digits)
        
        # If all the chars in the password are just digits, then penalize by the 
        # factor of length of the password
        if self.password_length == digit_count:
            return - 1 * self.password_length
        
        # Else do not penalize (show mercy)
        return 0

    # Score on basis of password length
    def length_score(self):
        return 4 * self.password_length
            
    # Count the number of uppercase & lower case characters
    def count_char_type(self, char_type):
        chartype_count = 0

        for char in self.password:
            if char in char_type:
                chartype_count = chartype_count + 1
        
        return chartype_count
    
    # Score on basis of password length
    def upper_lower_case_score(self):
        no_of_upper = self.count_char_type(string.ascii_uppercase)
        no_of_lower = self.count_char_type(string.ascii_lowercase)
        
        if not no_of_upper:
            upper_score = 0

        else:
            upper_score = 2 * (self.password_length - no_of_upper)

        if not no_of_lower:
            lower_score = 0

        else:
            lower_score = 2 * (self.password_length - no_of_lower)
        
        if upper_score and lower_score:
            return upper_score + lower_score

        # Otherwise (if either upper or lower score is 0)
        return 0
    
    def numerical_digits_score(self):
        digit_count = self.count_char_type(string.digits)
        return 4 * digit_count
    
    def special_char_score(self):
        special_char_count = self.count_char_type(string.punctuation)
        return  6 * special_char_count

    def middle_numbers_special_score(self):
        middle_chars_count = 0
        
        special_chartype = string.punctuation
        numerical_chartype = string.digits
        
        # All characters except 1st & last
        for char in self.password[1:-1]:
            if char in special_chartype or numerical_chartype:
                middle_chars_count = middle_chars_count + 1
        
        return 2 * middle_chars_count
    
    def repeating_chars_score(self):

        number_of_unique_chars = len(set(self.password))
        repeating_chars_penalty = self.password_length - number_of_unique_chars
        
        return -1 * repeating_chars_penalty

    def consecutive_upper_case_score(self):
        upper_case_chartype = string.ascii_lowercase
        upper_case_chartype_count = 0

        # Compare characters pair-wise (ex: 0-1, 1-2,..)
        for char_1, char_2 in zip(self.password, self.password[1:]):
            if char_1 in upper_case_chartype and char_2 in upper_case_chartype:
                upper_case_chartype_count = upper_case_chartype_count + 1

        return 2 * upper_case_chartype_count

    def consecutive_lower_case_score(self):
        lower_case_chartype = string.ascii_lowercase
        lower_case_chartype_count = 0

        # Compare characters pair-wise (ex: 0-1, 1-2,..)
        for char_1, char_2 in zip(self.password, self.password[1:]):
            if char_1 in lower_case_chartype and char_2 in lower_case_chartype:
                lower_case_chartype_count = lower_case_chartype_count + 1

        return 2 * lower_case_chartype_count

    def consecutive_numbers_score(self):
        digit_chartype = string.digits
        digit_chartype_count = 0

        # Compare characters pair-wise (ex: 0-1, 1-2,..)
        for char_1, char_2 in zip(self.password, self.password[1:]):
            if char_1 in digit_chartype and char_2 in digit_chartype:
                digit_chartype_count = digit_chartype_count + 1

        return 2 * digit_chartype_count

    def sequential_numbers_score(self):
        sequential_number_count = 0
        
        for i in range(100):
            if str(i) + str(i + 1) in self.password:
                sequential_number_count = sequential_number_count + 2

        return 2 * (- 1 * sequential_number_count)
    
    def check_password_strength(self):
        password_strength_score = sum((
                                    self.letters_only_score(),
                                    self.numbers_only_score(),
                                    self.upper_lower_case_score(),
                                    self.special_char_score(),
                                    self.numerical_digits_score(),
                                    self.length_score(),
                                    self.middle_numbers_special_score(),
                                    self.repeating_chars_score(),
                                    self.consecutive_upper_case_score(),
                                    self.consecutive_lower_case_score(),
                                    self.consecutive_numbers_score(),
                                    self.sequential_numbers_score(),
                                ))
        return password_strength_score