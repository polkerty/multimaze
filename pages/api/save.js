// Next.js API route support: https://nextjs.org/docs/api-routes/introduction

export default async (req, res) => {

  // We've got a payload

  const payload = JSON.parse(req.body);

  console.log(payload);

  console.log(process.env.SAVE_ENDPOINT);

  const submitResults = await fetch(process.env.SAVE_ENDPOINT, {
    method: 'POST',
    body: JSON.stringify(payload)
  }).then(x => x.text())

  console.log("API submit results: ", submitResults);
  res.statusCode = 200;
  res.json({ ok: true });
}