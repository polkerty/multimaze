// Next.js API route support: https://nextjs.org/docs/api-routes/introduction

export default (req, res) => {

  // We've got a payload

  const payload = JSON.parse(req.body);

  console.log(payload);

  console.log(process.env.SAVE_ENDPOINT);
  res.statusCode = 200
  res.json({ ok: true });
}
