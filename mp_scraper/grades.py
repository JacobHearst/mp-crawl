import logging
import re


class Grade:
    def __init__(self, grade):
        self.grade = grade


class YDS(Grade):
    static_indexes = ["3rd", "4th", "Easy 5th"]
    single_digit_mplier = 3
    double_digit_mplier = 7

    def index(self):
        """ Get the sorting index for a YDS grade
        Each grade from 5.0 to 5.9 is defined as having 3 potential values ordered as follows: 5.x-, 5.x, 5.x+
        Each grade 5.10 and above is defined as having 8 potential values ordered as follows: 5.xxa, 5.xxa/b, 5.xxb, 5.xxb/c, 5.xx, 5.xxc, 5.xxc/d, 5.xxd
        -/+ grades for 5.10 and above are treated as equal to 5.xxa/b and 5.xxc/d respectively
        5.xx grades are treated as equal to 5.xxb/c
        """
        if self.grade in self.static_indexes:
            return self.static_indexes.index(self.grade)

        # Remove the '5.' prefix
        fifth_grade = self.grade[2:]

        # Start after last position of static_indexes
        index = len(self.static_indexes)

        if len(fifth_grade) == 1:
            # 5.x case
            index += int(fifth_grade) * self.single_digit_mplier + 1
        elif not fifth_grade[1].isdigit():
            # 5.x +/- case
            offset = 1  # An offset of 1 brings us to the index for 5.x
            # Add 1 for 5.x+, subtract for 5.x-
            offset += 1 if fifth_grade[1] == "+" else -1

            index += int(fifth_grade[0]) * self.single_digit_mplier + offset
        else:
            # 5.xx case
            index += 29  # Start after last position of single digit grades
            offset = 4  # An offset of 4 brings us to the index for 5.xxb/c

            if fifth_grade[-1] == "a":
                # 5.xxa
                offset -= 3
            elif "a/b" in fifth_grade or "-" in fifth_grade:
                # 5.xxa/b or 5.xx-
                offset -= 2
            elif fifth_grade[-1] == "b":
                # 5.xxb
                offset -= 1
            elif "b/c" in fifth_grade or fifth_grade[-1].isdigit():
                # 5.xxb/c or 5.xx
                pass
            elif fifth_grade[-1] == "c":
                # 5.xxc
                offset += 1
            elif "c/d" in fifth_grade or "+" in fifth_grade:
                # 5.xxc/d or 5.xx+
                offset += 2
            elif fifth_grade[-1] == "d":
                # 5.xxd
                offset += 3
            else:
                logging.error(f"Unrecognized grade format {self.grade}")

            index += int(fifth_grade[1]) * self.double_digit_mplier + offset

        return index


class Hueco(Grade):
    def index(self):
        """Get the sorting index for a Hueco grade

        Indexing goes from VB to V17
        Each grade is defined as having 3 potential values ordered as follows: Vx-, Vx, Vx+
        Vx-y grades are treated as equal to Vx+
        V-easy grades are treated as equal to VB
        """
        if self.grade in ["V-easy", "VB"]:
            return 0

        # Remove the 'V' prefix
        v_grade = self.grade[1:]

        number_grade = None
        offset = 1  # An offset of 1 brings us to the index for Vx

        if all(char.isdigit() for char in v_grade):
            # Vx or Vxx
            number_grade = int(v_grade)
        elif re.match(r"\d+-\d+", v_grade) is not None:
            # Vx-y
            number_grade = int(re.match(r"(\d+)-\d+", v_grade)[1])
            offset += 1  # An offset of 2 brings us to the index for Vx+
        elif "+" in v_grade:
            # Vx+
            number_grade = int(v_grade[:-1])
            offset += 1
        elif "-" in v_grade:
            # Vx-
            number_grade = int(v_grade[:-1])
            offset -= 1  # An offset of 0 brings us to the index for Vx-
        else:
            logging.error(f"Unrecognized grade pattern {self.grade}")

        return number_grade * 3 + offset + 1  # Add 1 to account for VB/V-easy


class Ice(Grade):
    def index(self):
        """Get the sorting index for an Ice climbing grade
        Indexing goes from WI1-WI8
        Each grade is defined as having 3 potential values ordered as follows: WIx-, WIx, WIx+
        WIx-y grades are treated as equal to WIx+ 
        AIx grades are treated as equal to WIx
        """

        # Remove the 'WI'/'AI' prefix
        ice_grade = self.grade[2:]

        number_grade = None
        offset = 1  # An offset of 1 brings us to the index for Ix

        if all(char.isdigit() for char in ice_grade):
            # Ix
            number_grade = int(ice_grade)
        elif re.match(r"\d+-\d+", ice_grade) is not None:
            # Ix-y
            number_grade = int(re.match(r"(\d+)-\d+", ice_grade)[1])
            offset += 1  # An offset of 2 brings us to the index for Ix+
        elif "+" in ice_grade:
            # Ix+
            number_grade = int(ice_grade[:-1])
            offset += 1
        elif "-" in ice_grade:
            # Ix-
            number_grade = int(ice_grade[:-1])
            offset -= 1  # An offset of 0 brings us to the index for Ix-
        else:
            logging.error(f"Unrecognized grade pattern {self.grade}")

        # Subtract 1 from the grade so that the range is 0-7 instead of 1-8
        return (number_grade - 1) * 3 + offset


class Aid(Grade):
    def index(self):
        """Get the sorting index for an Aid climbing grade
        Indexing goes from A1-A8
        Each grade is defined as having 3 potential values ordered as follows: Ax-, Ax, Ax+
        Cx grades are treated as equal to Ax
        """

        # Remove the 'A'/'C' prefix
        ice_grade = self.grade[1:]

        number_grade = None
        offset = 1  # An offset of 1 brings us to the index for Ax

        if all(char.isdigit() for char in ice_grade):
            # Ax
            number_grade = int(ice_grade)
        elif "+" in ice_grade:
            # Ax+
            number_grade = int(ice_grade[:-1])
            offset += 1
        elif "-" in ice_grade:
            # Ax-
            number_grade = int(ice_grade[:-1])
            offset -= 1  # An offset of 0 brings us to the index for Ax-
        else:
            logging.error(f"Unrecognized grade pattern {self.grade}")

        return number_grade * 3 + offset


class Mixed(Grade):
    def index(self):
        """Get the sorting index for an Ice climbing grade
        Indexing goes from M1-M9
        Each grade is defined as having 3 potential values ordered as follows: Mx-, Mx, Mx+
        Mx-y grades are treated as equal to Mx+
        """

        # Remove the 'M' prefix
        mixed_grade = self.grade[1:]

        number_grade = None
        offset = 1  # An offset of 1 brings us to the index for Mx

        if all(char.isdigit() for char in mixed_grade):
            # Mx
            number_grade = int(mixed_grade)
        elif re.match(r"\d+-\d+", mixed_grade) is not None:
            # Mx-y
            number_grade = int(re.match(r"(\d+)-\d+", mixed_grade)[1])
            offset += 1  # An offset of 2 brings us to the index for Mx+
        elif "+" in mixed_grade:
            # Mx+
            number_grade = int(mixed_grade[:-1])
            offset += 1
        elif "-" in mixed_grade:
            # Mx-
            number_grade = int(mixed_grade[:-1])
            offset -= 1  # An offset of 0 brings us to the index for Mx-
        else:
            logging.error(f"Unrecognized grade pattern {self.grade}")

        # Subtract 1 from the grade so that the range is 0-9 instead of 1-10
        return (number_grade - 1) * 3 + offset


class Snow(Grade):
    def index(self):
        return ["Easy Snow", "Mod. Snow", "Steep Snow"].index(self.grade)


class Danger(Grade):
    def index(self):
        return ["PG13", "R", "X"].index(self.grade)
