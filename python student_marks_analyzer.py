<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Weather App</title>

    <style>

        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #4facfe, #00f2fe);

            display: flex;
            justify-content: center;
            align-items: center;

            min-height: 100vh;
        }

        .container {
            background: white;
            width: 400px;
            padding: 30px;
            border-radius: 20px;
            text-align: center;

            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
        }

        h1 {
            color: #333;
            margin-bottom: 20px;
        }

        .search {
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
        }

        input {
            flex: 1;
            padding: 12px;

            font-size: 16px;

            border: 1px solid #ccc;
            border-radius: 8px;
        }

        button {
            padding: 12px 18px;

            border: none;
            border-radius: 8px;

            background: #2196f3;
            color: white;

            font-size: 15px;
            cursor: pointer;
        }

        button:hover {
            background: #1976d2;
        }

        #error {
            color: red;
        }

        #weather {
            display: none;
        }

        #weatherIcon {
            width: 100px;
        }

        #city {
            font-size: 28px;
            font-weight: bold;
            color: #333;
        }

        #country {
            color: #777;
            margin: 5px;
        }

        #localTime {
            font-size: 16px;
            font-weight: bold;
            color: #555;

            margin: 10px 0 20px;
        }

        #temperature {
            font-size: 50px;
            font-weight: bold;
            color: #2196f3;

            margin: 10px;
        }

        #condition {
            font-size: 20px;
            color: #555;

            margin-bottom: 20px;
        }

        .details {
            display: grid;

            grid-template-columns: 1fr 1fr;

            gap: 10px;
        }

        .box {
            background: #f2f2f2;

            padding: 15px;

            border-radius: 10px;
        }

        .box p {
            margin: 5px;
        }

        .label {
            color: #777;
            font-size: 14px;
        }

        .value {
            font-weight: bold;
            font-size: 17px;
        }

    </style>

</head>


<body>


<div class="container">

    <h1>🌤️ Weather App</h1>


    <div class="search">

        <input
            type="text"
            id="cityInput"
            placeholder="Enter city"
            value="London"
        >

        <button onclick="getWeather()">
            Search
        </button>

    </div>


    <p id="error"></p>


    <div id="weather">

        <img
            id="weatherIcon"
            alt="Weather icon"
        >


        <div id="city"></div>

        <div id="country"></div>


        <!-- Local Time -->

        <div id="localTime">
            🕐 Loading time...
        </div>


        <div id="temperature"></div>

        <div id="condition"></div>


        <div class="details">


            <div class="box">

                <p class="label">
                    Feels Like
                </p>

                <p
                    class="value"
                    id="feelsLike"
                ></p>

            </div>


            <div class="box">

                <p class="label">
                    Humidity
                </p>

                <p
                    class="value"
                    id="humidity"
                ></p>

            </div>


            <div class="box">

                <p class="label">
                    Wind
                </p>

                <p
                    class="value"
                    id="wind"
                ></p>

            </div>


            <div class="box">

                <p class="label">
                    UV Index
                </p>

                <p
                    class="value"
                    id="uv"
                ></p>

            </div>


        </div>

    </div>

</div>


<script>

    const API_KEY =
        "1e3f9f1a66ea4080a8c153043260510";


    let cityTimeZone = null;


    async function getWeather() {

        const city =
            document.getElementById("cityInput")
            .value
            .trim();


        const error =
            document.getElementById("error");


        const weather =
            document.getElementById("weather");


        if (city === "") {

            error.innerText =
                "Please enter a city name.";

            weather.style.display =
                "none";

            return;
        }


        error.innerText =
            "Loading...";


        try {

            const url =
                "https://api.weatherapi.com/v1/current.json" +
                "?key=" + API_KEY +
                "&q=" + encodeURIComponent(city) +
                "&aqi=yes";


            const response =
                await fetch(url);


            const data =
                await response.json();


            if (!response.ok || data.error) {

                throw new Error(
                    data.error?.message ||
                    "Unable to get weather data"
                );

            }


            // City

            document.getElementById("city")
                .innerText =
                data.location.name;


            // Country

            document.getElementById("country")
                .innerText =
                data.location.country;


            // Timezone

            cityTimeZone =
                data.location.tz_id;


            // Temperature

            document.getElementById("temperature")
                .innerText =
                Math.round(data.current.temp_c) + "°C";


            // Condition

            document.getElementById("condition")
                .innerText =
                data.current.condition.text;


            // Weather icon

            document.getElementById("weatherIcon")
                .src =
                "https:" +
                data.current.condition.icon;


            // Feels like

            document.getElementById("feelsLike")
                .innerText =
                Math.round(data.current.feelslike_c) +
                "°C";


            // Humidity

            document.getElementById("humidity")
                .innerText =
                data.current.humidity + "%";


            // Wind

            document.getElementById("wind")
                .innerText =
                data.current.wind_kph +
                " km/h";


            // UV

            document.getElementById("uv")
                .innerText =
                data.current.uv;


            // Show weather

            weather.style.display =
                "block";


            error.innerText = "";


            updateClock();

        }


        catch (err) {

            console.error(err);

            error.innerText =
                "Error: " + err.message;

            weather.style.display =
                "none";

        }

    }


    // Live clock

    function updateClock() {

        if (!cityTimeZone) {
            return;
        }


        const now = new Date();


        const time =
            new Intl.DateTimeFormat(
                "en-US",
                {
                    timeZone: cityTimeZone,

                    hour: "2-digit",
                    minute: "2-digit",
                    second: "2-digit",

                    hour12: true
                }
            ).format(now);


        const date =
            new Intl.DateTimeFormat(
                "en-US",
                {
                    timeZone: cityTimeZone,

                    weekday: "long",
                    year: "numeric",
                    month: "long",
                    day: "numeric"
                }
            ).format(now);


        document.getElementById("localTime")
            .innerText =
            "🕐 " + time + " | " + date;

    }


    // Update time every second

    setInterval(
        updateClock,
        1000
    );


    // Load London when page opens

    getWeather();

</script>


</body>

</html>
