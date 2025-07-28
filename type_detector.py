# type_detector.py

from datetime import datetime
import re
import numpy as np

class DataTypeDetector:
    def __init__(self):
        pass

    def detect_column_type(self, series):
        """
        Detects the type of a column: 'date', 'number', or 'string'
        Returns a dictionary: {'type': ..., 'confidence': ...}
        """
        data = series.dropna().astype(str).tolist()

        if not data:
            return {'type': 'unknown', 'confidence': 0}

        date_count = 0
        number_count = 0

        for value in data:
            if self.is_date(value):
                date_count += 1
            elif self.is_number(value):
                number_count += 1

        total = len(data)
        date_conf = date_count / total
        num_conf = number_count / total

        if date_conf > 0.6:
            return {'type': 'date', 'confidence': round(date_conf, 2)}
        elif num_conf > 0.6:
            return {'type': 'number', 'confidence': round(num_conf, 2)}
        else:
            return {'type': 'string', 'confidence': round(1 - max(date_conf, num_conf), 2)}

    def is_date(self, value):
        """
        Check if the value looks like a date
        """
        date_formats = [
            "%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y", "%d-%b-%Y",
            "%d-%m-%Y", "%b %Y", "%B %Y"
        ]
        for fmt in date_formats:
            try:
                datetime.strptime(value, fmt)
                return True
            except:
                continue
        # Excel serial number handling
        if re.match(r'^\d{5}$', value):
            return True
        return False

    def is_number(self, value):
        """
        Check if the value is numeric (considering symbols like $, commas, etc.)
        """
        cleaned = re.sub(r'[^\d.-]', '', value)
        try:
            float(cleaned)
            return True
        except:
            return False
