import React from "react";
import { useGetAllMarkers } from "@/apiQueries/queries";
import { Card, CardHeader } from "@/components/ui/card";
import { Link } from "react-router-dom";

const Home = () => {
  const { markers, isLoading, isError, isSuccess } = useGetAllMarkers();

  console.log("Markers data:", markers);

  if (isLoading) {
    return <div className="container mx-auto w-full">Loading markers...</div>;
  }

  if (isError) {
    return (
      <div className="container mx-auto w-full">Error loading markers</div>
    );
  }

  return (
    <div className="container mx-auto w-full flex flex-col gap-4 items-center">
      <div className="flex gap-2 items-center">
        {markers.map((marker) => {
          return (
            <Link to={`/marker/${marker.markerId}`}>
              <Card key={marker.markerId}>
                <CardHeader>
                  {marker.markerId} • {marker.status}
                </CardHeader>
              </Card>
            </Link>
          );
        })}
      </div>
    </div>
  );
};

export default Home;
