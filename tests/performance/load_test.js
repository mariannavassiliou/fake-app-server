import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
 vus: 10,
 duration: '5s',
 summaryTrendStats: ['avg', 'p(95)', 'p(99)']};

export default function () {
  http.get('http://127.0.0.1:5001/people/1');
  const res = http.get('http://127.0.0.1:5001/people/1');
  check(res, {
    'is status 200': (r) => r.status === 200,
    'response body is valid': (r) => r.body.includes("Luke Skywalker"),
  });
  console.log('Response time was ' + String(res.timings.duration) + ' ms');
  // const fs  = require('fs').promises;
  // fs.appendFile('myFile.txt',String(res.timings.duration))
}