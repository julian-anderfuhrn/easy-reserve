import { Link } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

export default function Header() {
  const { isAuthenticated, logout } = useAuth();

  return (
    <header className="bg-white shadow-sm sticky top-0 z-50">
      <nav className="max-w-6xl mx-auto px-6 py-4 flex items-center justify-between">

        {/* LOGO */}
        <Link to="/" className="text-xl font-bold text-blue-600">
          EasyReserve
        </Link>

        {/* NAV LINKS */}
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

        {/* AUTH */}
        <div className="flex items-center gap-4 text-sm">
          {isAuthenticated ? (
            <>
              <Link
                to="/dashboard"
                className="font-medium text-gray-700 hover:text-blue-600 transition"
              >
                Dashboard
              </Link>

              <button
                onClick={logout}
                className="hover:text-red-700 font-medium transition"
              >
                Log out
              </button>
            </>
          ) : (
            <Link
              to="/login"
              className="text-gray-500 hover:text-gray-700 transition"
            >
              Professional access
            </Link>
          )}
        </div>

      </nav>
    </header>
  );
}
