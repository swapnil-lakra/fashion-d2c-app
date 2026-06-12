export default async function ProductsPage() {
  const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/products/`, {
    cache: "no-store", // or 'force-cache' for static
  });
  const products = await res.json();

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-3xl font-bold mb-6">Our Collection</h1>
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
        {products.map((product) => (
          <div key={product.id} className="border rounded-lg p-4 shadow">
            <img src={product.image_url} alt={product.name} className="w-full h-48 object-cover rounded" />
            <h2 className="text-xl font-semibold mt-2">{product.name}</h2>
            <p className="text-gray-600">₹{product.price}</p>
          </div>
        ))}
      </div>
    </div>
  );
}