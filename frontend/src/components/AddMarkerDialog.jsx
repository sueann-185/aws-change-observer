import React from "react";
import {
  Dialog,
  DialogTrigger,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogDescription,
} from "@/components/ui/dialog";

const AddMarkerDialog = ({ isOpen, setIsOpen }) => {
  return (
    <Dialog open={isOpen} onOpenChange={setIsOpen}>
      <DialogContent>
        <DialogHeader>
          <DialogTitle>Add a new marker</DialogTitle>
          FORM
          <DialogDescription>GOOGLE MAPS API</DialogDescription>
        </DialogHeader>
      </DialogContent>
    </Dialog>
  );
};

export default AddMarkerDialog;
