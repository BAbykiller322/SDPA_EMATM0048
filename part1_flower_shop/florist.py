from Constants import florist_salary,florist_working_hours,bouquet_time_required
import math

class Florist:
    """Represent a single florist with optional bouquet-specific speed talents."""
    def __init__(self,name,talents:dict[str, int] = None):
        """
        Init a florist.

        Inputs:
        name: non-empty string identifier.
        talents: optional mapping {bouquet_name: time_ratio in (0,1]} applied to base craft time.

        Raises:
        ValueError if name is empty/whitespace or any ratio is outside (0,1].
        """
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Florist name must be non-empty string type.")
        self.name = name.strip()
        if talents:
            clean_talents = {}
            for bouquet, ratio in talents.items():
                if ratio <= 0 or ratio > 1:
                    raise ValueError(
                        f"Talent ratio for {bouquet} of {self.name} must be in (0, 1]"
                    )
                clean_talents[bouquet] = ratio
            self.talents = clean_talents
        else:
            self.talents = {}

    def monthly_cost(self):
        """
        Return the monthly labor cost for this florist.

        Output:
        hourly_salary * working_hours_per_month.
        """
        return florist_salary * florist_working_hours

    def time_required(self,bouquet:str):
        """
        Compute minutes needed for a bouquet.

        Inputs:
        bouquet: name key found in bouquet_time_required.

        Calculation:
        base_time = bouquet_time_required[bouquet] (minutes per unit).
        ratio = self.talents.get(bouquet, 1.0) to speed up/slightly reduce time.
        use ceil to keep integer minutes.

        Output:
        int minutes required for this florist to craft one bouquet of the given type.
        """
        base_time = bouquet_time_required[bouquet]
        ratio = self.talents.get(bouquet, 1.0)
        return math.ceil(base_time * ratio)

