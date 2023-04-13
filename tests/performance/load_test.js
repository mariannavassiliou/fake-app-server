import http from 'k6/http';
import { check, sleep } from 'k6';
let url = 'http://127.0.0.1:5001/people/1';
let bodyResponse = "Luke Skywalker";

export const options = {
 vus: 10,
 duration: '60s',
 summaryTrendStats: ['avg', 'p(95)', 'p(99)']};

export default function () {
  http.get(url);
  const res = http.get(url);
  check(res, {
    'is status 200': (r) => r.status === 200,
    'response body is valid': (r) => r.body.includes(bodyResponse),
  });
}