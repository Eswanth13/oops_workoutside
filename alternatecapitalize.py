class Altcap:
    def reverse_cap_upper(self,string):
        FormattedString = ""
        for (position,ch) in enumerate(string):
            if position % 2 == 0:
                FormattedString = FormattedString + str(ch).upper()
            else:
                FormattedString = FormattedString + str(ch).lower()
        return FormattedString

    def reverse_cap_lower(self,string):
        FormattedString = ""
        for (position,ch) in enumerate(string):
            if position % 2 == 0:
                FormattedString = FormattedString + str(ch).lower()
            else:
                FormattedString = FormattedString + str(ch).upper()
        return FormattedString


