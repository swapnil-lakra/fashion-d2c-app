export default async function Home() {
  const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/products/featured?limit=4`);
  const featured = await res.json();

  return (
    <div>
      <section className="text-center py-16 bg-gray-100">
        <h1 className="text-5xl font-bold">D2C Fashion</h1>
        <p className="text-lg mt-2">No middlemen, just style.</p>
      </section>
      <section className="container mx-auto py-10">
        <h2 className="text-2xl font-bold mb-6">Featured</h2>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
          {featured.map(product => (
            <div key={product.id}>{product.name}</div>
          ))}
        </div>
      </section>
    </div>
  );
}