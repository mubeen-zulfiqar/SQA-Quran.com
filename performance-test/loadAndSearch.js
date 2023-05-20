import http from "k6/http";
import { check, group, sleep } from "k6";

export let options = {
  vus: 10, // number of virtual users
  duration: "30s", // duration of the test
  thresholds: {
    http_req_duration: ["p(95)<500"], // 95% of requests should be below 500ms
  },
};

export default function () {
  group("Home Page", function () {
    let res = http.get("https://quran.com/");
    check(res, { "Home page loaded successfully": (r) => r.status === 200 });
  });

  group("Search for a Surah", function () {
    let res = http.get("https://quran.com/search?q=al-fatiha");
    check(res, { "Search page loaded successfully": (r) => r.status === 200 });

    sleep(1); // wait for 1 second before making the search request

    let searchRes = http.get("https://quran.com/api/v4/search?q=al-fatiha");
    check(searchRes, { "Search for Surah Al-Fatiha": (r) => r.status === 200 });
  });
}
