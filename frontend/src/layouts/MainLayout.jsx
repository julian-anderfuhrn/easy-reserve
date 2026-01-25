// import Header from "../components/Header";
import Footer from "../components/Footer";

export default function MainLayout({ children }) {
  return (
    <div className="bg-gray-100 min-h-screen flex flex-col">
      {/* <Header /> */}

      <main className="flex-1 container mx-auto p-4">
        {children}
      </main>

      <Footer />
    </div>
  );
}
