"""Constants for the Smart Irrigation integration."""

DOMAIN = "smart_irrigation"
NAME = "Smart Irrigation"
DOMAIN_DATA = f"{DOMAIN}_data"
VERSION = "0.0.29"

ISSUE_URL = "https://github.com/jeroenterheerdt/HASmartIrrigation/issues"

# Icons
ICON = "mdi:sprinkler"

# Platforms
SENSOR = "sensor"
PLATFORMS = [SENSOR]

# Configuration and options
CONF_API_KEY = "api_key"
CONF_REFERENCE_ET = "reference_evapotranspiration"
CONF_REFERENCE_ET_1 = "reference_evapotranspiration_1"
CONF_REFERENCE_ET_2 = "reference_evapotranspiration_2"
CONF_REFERENCE_ET_3 = "reference_evapotranspiration_3"
CONF_REFERENCE_ET_4 = "reference_evapotranspiration_4"
CONF_REFERENCE_ET_5 = "reference_evapotranspiration_5"
CONF_REFERENCE_ET_6 = "reference_evapotranspiration_6"
CONF_REFERENCE_ET_7 = "reference_evapotranspiration_7"
CONF_REFERENCE_ET_8 = "reference_evapotranspiration_8"
CONF_REFERENCE_ET_9 = "reference_evapotranspiration_9"
CONF_REFERENCE_ET_10 = "reference_evapotranspiration_10"
CONF_REFERENCE_ET_11 = "reference_evapotranspiration_11"
CONF_REFERENCE_ET_12 = "reference_evapotranspiration_12"
CONF_NUMBER_OF_SPRINKLERS = "number_of_sprinklers"
CONF_FLOW = "flow"
CONF_AREA = "area"
CONF_THROUGHPUT = "throughput"
CONF_PEAK_ET = "peak_evapotranspiration"
CONF_SYSTEM_OF_MEASUREMENT = "system_of_measurement"
CONF_PRECIPITATION_RATE = "precipitation_rate"
CONF_RAIN = "rain"
CONF_SNOW = "snow"
CONF_PRECIPITATION = "precipitation"
CONF_EVAPOTRANSPIRATION = "evapotranspiration"
CONF_WATER_BUDGET = "water_budget"
CONF_BUCKET = "bucket"
CONF_NETTO_PRECIPITATION = "netto_precipitation"
CONF_LEAD_TIME = "lead_time"
CONF_MAXIMUM_DURATION = "maximum_duration"
CONF_FORCE_MODE_DURATION = "force_mode_duration"
CONF_ADJUSTED_RUN_TIME_MINUTES = "adjusted_run_time_minutes"
CONF_BASE_SCHEDULE_INDEX_MINUTES = "base_schedule_index_minutes"
CONF_SHOW_UNITS = "show_units"
CONF_AUTO_REFRESH = "auto_refresh"
CONF_AUTO_REFRESH_TIME = "auto_refresh_time"
CONF_NAME = "name"
CONF_CONFIG = "config"
CONF_SOURCE_SWITCHES = "sources"
CONF_SENSORS = "sensors"
CONF_FORCE_MODE_ENABLED = "force_mode_enabled"

# Settings switches (True = OWM, False is own sensors)
CONF_SWITCH_SOURCE_PRECIPITATION = "use_owm_precipitation"
CONF_SWITCH_SOURCE_DAILY_TEMPERATURE = "use_owm_temperature"
CONF_SWITCH_SOURCE_MINIMUM_TEMPERATURE = "use_owm_min_temperature"
CONF_SWITCH_SOURCE_MAXIMUM_TEMPERATURE = "use_owm_max_temperature"
CONF_SWITCH_SOURCE_DEWPOINT = "use_owm_dewpoint"
CONF_SWITCH_SOURCE_PRESSURE = "use_owm_pressure"
CONF_SWITCH_SOURCE_HUMIDITY = "use_owm_humidity"
CONF_SWITCH_SOURCE_WINDSPEED = "use_owm_windspeed"

# Sensors setting labels
CONF_SENSOR_PRECIPITATION = "sensor_precipitation"
CONF_SENSOR_DAILY_TEMPERATURE = "sensor_temperature"
CONF_SENSOR_DEWPOINT = "sensor_dewpoint"
CONF_SENSOR_HUMIDITY = "sensor_humidity"
CONF_SENSOR_MAXIMUM_TEMPERATURE = "sensor_max_temperature"
CONF_SENSOR_MINIMUM_TEMPERATE = "sensor_min_temperature"
CONF_SENSOR_PRESSURE = "sensor_pressure"
CONF_SENSOR_WINDSPEED = "sensor_windspeed"

# Events
EVENT_BUCKET_UPDATED = "bucket_updated_event"
EVENT_HOURLY_DATA_UPDATED = "hourly_updated_event"
EVENT_FORCE_MODE_TOGGLED = "force_mode_toggle_event"

# Services
SERVICE_RESET_BUCKET = "reset_bucket"
SERVICE_CALCULATE_DAILY_ADJUSTED_RUN_TIME = "calculate_daily_adjusted_run_time"
SERVICE_CALCULATE_HOURLY_ADJUSTED_RUN_TIME = "calculate_hourly_adjusted_run_time"
SERVICE_ENABLE_FORCE_MODE = "enable_force_mode"
SERVICE_DISABLE_FORCE_MODE = "disable_force_mode"

# Systems of measurement
SETTING_METRIC = "metric"
SETTING_US = "us"

# METRIC TO IMPERIAL (US) FACTORS
MM_TO_INCH_FACTOR = 0.03937008
LITER_TO_GALLON_FACTOR = 0.26417205
M2_TO_SQ_FT_FACTOR = 10.7639104
M_TO_FT_FACTOR = 3.2808399
KMH_TO_MS_FACTOR = 3.6
MILESH_TO_MS_FACTOR = 2.23693629
PSI_TO_HPA_FACTOR = 0.0145037737796859
# Defaults
DEFAULT_NAME = NAME

# Types
TYPE_PRECIPITATION = "Precipitation"
TYPE_RAIN = "Rain"
TYPE_SNOW = "Snow"
TYPE_THROUGHPUT = "Throughput"
TYPE_PEAK_ET = "Peak Evapotranspiration"
TYPE_PRECIPITATION_RATE = TYPE_PRECIPITATION + " Rate"
TYPE_BASE_SCHEDULE_INDEX = "Base Schedule Index"
TYPE_EVAPOTRANSPIRATION = "Evapotranspiration"
TYPE_ADJUSTED_RUN_TIME = "Daily Adjusted Run Time"
TYPE_CURRENT_ADJUSTED_RUN_TIME = "Hourly Adjusted Run Time"

# UNITS
UNIT_OF_MEASUREMENT_SECONDS = "s"
UNIT_OF_MEASUREMENT_MINUTES = "min"
UNIT_OF_MEASUREMENT_UNKNOWN = "unknown"
UNIT_OF_MEASUREMENT_LITERS = "l"
UNIT_OF_MEASUREMENT_GALLONS = "gallon"
UNIT_OF_MEASUREMENT_MMS = "mm"
UNIT_OF_MEASUREMENT_INCHES = "inch"
UNIT_OF_MEASUREMENT_M2 = "m2"
UNIT_OF_MEASUREMENT_SQ_FT = "sq ft"
UNIT_OF_MEASUREMENT_INCHES_HOUR = "inch/hour"
UNIT_OF_MEASUREMENT_MMS_HOUR = "mm/hour"
UNIT_OF_MEASUREMENT_GPM = "gallon/minute"
UNIT_OF_MEASUREMENT_LPM = "liter/minute"

# OPTIONS DEFAULTS
DEFAULT_LEAD_TIME = 0
DEFAULT_MAXIMUM_DURATION = -1
DEFAULT_FORCE_MODE_DURATION = 0
DEFAULT_SHOW_UNITS = False
DEFAULT_AUTO_REFRESH = True
DEFAULT_AUTO_REFRESH_TIME = "23:00"

STARTUP_MESSAGE = f"""
-------------------------------------------------------------------
{NAME}
Version: {VERSION}
If you have any issues with this you need to open an issue here:
{ISSUE_URL}
-------------------------------------------------------------------
"""
