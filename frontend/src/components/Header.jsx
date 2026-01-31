import { Link } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

export default function Header() {
  const { user, loading } = useAuth();

  if (loading) return null;

  return (
    <header className="bg-white shadow-sm sticky top-0 z-50">
      <nav className="max-w-6xl mx-auto px-6 py-4 flex items-center justify-between">

        <Link to="/" className="text-xl font-bold text-blue-600">
          EasyReserve
        </Link>

        <div className="hidden md:flex items-center gap-6 text-sm font-medium text-gray-700">
          <Link to="/" className="hover:text-blue-600 transition">
            Home
          </Link>

          <Link
            to="/appointments"
            className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-lg font-semibold transition"
          >
            Book appointment
          </Link>
        </div>

        <div className="flex items-center gap-4 text-sm">
          {user ? (
            <>
              <Link to="/dashboard" className="font-medium hover:text-blue-600">
                Dashboard
              </Link>
              <button className="hover:text-red-600">
                Log out
              </button>
            </>
          ) : (
            <Link to="/login" className="text-gray-500 hover:text-gray-700">
              Professional access
            </Link>
          )}
        </div>
      </nav>
    </header>
  );
}
