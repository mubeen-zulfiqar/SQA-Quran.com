import http from "k6/http";
import { check, sleep } from "k6";

export let options = {
  vus: 10,
  duration: "30s",
  thresholds: {
    http_req_duration: ["p(95)<500"], // 95% of requests should be under 500ms
    http_req_failed: ["rate<0.01"], // Failed requests should be less than 1%
  },
};

export default function () {
  // Step 1: Open the surah page
  let res = http.get("https://quran.com/1");

  // Check that the response code is 200 OK
  check(res, {
    "status is 200": (r) => r.status === 200,
  });

  // Wait for 2 seconds before making the next request
  sleep(2);

  // Step 2: Change the language of the translation
  res = http.post("https://quran.com/api/v4/chapters/1/languages", {
    language: "ur",
  });

  // Check that the response code is 200 OK
  check(res, {
    "status is 200": (r) => r.status === 200,
  });

  // Wait for 2 seconds before making the next request
  sleep(2);
}
