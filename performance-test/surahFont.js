import http from "k6/http";
import { check, sleep } from "k6";

export let options = {
  stages: [
    { duration: "30s", target: 50 },
    { duration: "1m", target: 100 },
    { duration: "30s", target: 0 },
  ],
};

export default function () {
  // Send GET request to surah page
  let res = http.get("https://quran.com/1");

  // Check response status code is 200
  check(res, { "status is 200": (r) => r.status === 200 });

  // Sleep for 3 seconds to allow page to fully load
  sleep(3);

  // Send POST request to change font size from 3 to 7
  res = http.post(
    "https://quran.com/api/settings",
    '{"fontSize":7,"fontFamily":"UthmanicHafs1Ver11"}',
    {
      headers: {
        "Content-Type": "application/json",
      },
    }
  );

  // Check response status code is 200
  check(res, { "status is 200": (r) => r.status === 200 });

  // Sleep for 3 seconds to allow page to fully load with new font size
  sleep(3);
}
